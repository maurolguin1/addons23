# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Candidroot Solutions Pvt. Ltd.
# See LICENSE file for full copyright and licensing details.

{
    'name': 'Barcode Scan With Weight Screen',
    'version': '10.0.1.0.0',
    'category': 'Point Of Sale',
    'author': 'Candidroot Solutions Pvt. Ltd.',
    'license': 'AGPL-3',
    'website': 'https://www.candidroot.com',
    'summary': 'Barcode Scan With Weight Screen',
    'description': """
                    Open weight screen when you scan the product with barcode if product has weight feature enable.
                    """,
    'depends': ['point_of_sale'],
    'data': ['views/barcode.xml'],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False
}