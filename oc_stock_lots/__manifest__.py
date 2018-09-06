# -*- coding: utf-8 -*-
# Part of eComBucket. See LICENSE file for full copyright and licensing details
{
    'name': "Stock Lots Customization",
    'category': 'Delivery',
    'author': "eComBucket",
    'version': '0.1',
    'maintainer': 'support@ecombucket.zohosupport.com',
    'website':'https://twitter.com/ecombucket',
    'depends': ['stock', 'product_expiry'],
    'data': [
        "views/views.xml",
        "data/data.xml",
    ],
	'currency': 'EUR',
	'images': ['static/description/Banner.png'],
	'pre_init_hook': 'odoo_version_check',
	'installable': True,
	'application': True,
}
