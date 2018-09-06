# -*- coding: utf-8 -*-
######################################################################################################
#
# Copyright (C) B.H.C. sprl - All Rights Reserved, http://www.bhc.be
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied,
# including but not limited to the implied warranties
# of merchantability and/or fitness for a particular purpose
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from odoo import api, fields, models, _
import logging
_logger = logging.getLogger(__name__)

class res_partner(models.Model):
    _inherit = "res.partner"

    blacklist = fields.Char(string='Blacklist')

    @api.onchange('category_id')
    def onchange_category_id(self):
        bl=self.env['res.partner.category'].search([('blacklist','=',True)])
        if bl:
            blacklist=False
            for j in self.category_id:
                if j.blacklist == True:
                    blacklist = 1
            if blacklist == 1:
                self.sale_warn = 'block'
                self.blacklist = '1'
            else:
                self.sale_warn = 'no-message'
                self.blacklist = '0'

class category(models.Model):
    _inherit = "res.partner.category"

    blacklist = fields.Boolean(string='Blacklist')