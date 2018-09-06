# -*- coding: utf-8 -*-
# Part of eComBucket. See LICENSE file for full copyright and licensing details
import logging
import datetime
from odoo import api, fields, models
logger = logging.getLogger(__name__)


class Product(models.Model):
    _inherit = "product.product"
    lots_sequence = fields.Integer(default=0)

class StockMoveLine(models.Model):
    _inherit = "stock.move.line"
    active = fields.Boolean(default=True)
    @api.multi
    def write(self, vals):
        lot_id = vals.get('lot_id')
        for record in self:
            production_date = record.move_id.production_date
            if lot_id and production_date:
                lot_id = self.env['stock.production.lot'].browse(lot_id)
                mapped_fields = {
                    'life_date': 'life_time',
                    'use_date': 'use_time',
                    'removal_date': 'removal_time',
                    'alert_date': 'alert_time'
                }
                res = dict.fromkeys(mapped_fields, False)
                product = lot_id.product_id
                if product:
                    for field in mapped_fields:
                        duration = getattr(product, mapped_fields[field])
                        try:
                            date = fields.Datetime.from_string(production_date) + datetime.timedelta(days=duration)
                            res[field] = fields.Datetime.to_string(date)
                        except Exception as e:
                            pass
                res = {k:v for k,v in res.items() if v is not None}
                lot_id.write(res)
        return super(StockMoveLine, self).write(vals)

class Stock(models.Model):
    _inherit = "stock.move"
    lots_count = fields.Integer(copy=False)
    production_date = fields.Datetime(copy=False)
    active = fields.Boolean(default=True)

    @api.multi
    def write(self, vals):
        res = super(Stock, self).write(vals)
        for record in self:
            if vals.get('lots_count') and record.product_id:
                record.product_id.lots_sequence += vals.get('lots_count')
        return res

    @api.model
    def create(self, vals):
        res = super(Stock, self).create(vals)
        if vals.get('lots_count') and res.product_id:
            res.product_id.lots_sequence += vals.get('lots_count')
        return res

    def get_new_move_line(self, vals, qty_done, default_code, sequence, index):
        vals['qty_done'] = qty_done
        default_code = 'LT-%s-'%(default_code or '')
        sequence = default_code+'%04d'%(sequence)
        vals['lot_name'] = sequence
        return self.env['stock.move.line'].create(vals)

    @api.onchange('lots_count')
    def onchange_lots_count(self):
        lots_count = self.lots_count
        if lots_count:
            product_uom_qty = self.product_uom_qty
            default_code = self.product_id.default_code
            lots_sequence = self.product_id.lots_sequence
            lots_co = product_uom_qty//lots_count
            lots_lets = product_uom_qty%lots_count
            vals = self._prepare_move_line_vals()
            origin = self.move_line_ids
            move_line_ids = self.move_line_ids.filtered(lambda i:i.product_uom_qty and (i.qty_done==0))
            res = (origin-move_line_ids)
            if len(res):
                for rec in res:
                    #rec.unlink()
                    #rec.lot_name='DEL%s'%(rec.lot_name)
                    #rec.active = False
                    rec.sudo().write(dict(active=False,move_id=None, lot_name=None))
                #res.sudo().write(dict(active=False))
            move_line_ids  = move_line_ids.ids
            for index in range(1, lots_count+1):
                lots_sequence +=1
                if index == lots_count and lots_lets:
                    lots_co += lots_lets
                move_line = self.get_new_move_line(vals, lots_co, default_code, lots_sequence, index)
                move_line_ids +=[move_line.id]
            data = {
                'value': {
                    'move_line_ids': [
                        (6,0,move_line_ids),
                    ]
                }
            }
            return data
