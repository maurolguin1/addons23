# -*- coding: utf-8 -*-
##############################################################################
#
#    BITODOO Development SAC.
#    Copyright (C) 2016-TODAY BITODOO (<http://bitodoo.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Habilita menu de reporte Inventory at date para usuarios jefes de inventairo',
    'summary': 'Habilita menu de reporte Inventory at date para usuarios jefes de inventairo',
    'description': """Habilita menu de reporte Inventory at date para usuarios jefes de inventairo""",
    'category': 'Stock',
    'version': '1.0',
    'website': 'http://www.bitodoo.com/',
    'author': 'Bitodoo',
    'depends': [
        'stock_account',
    ],
    'data': [
        'views/menu.xml',
    ],
    'application': True,
}
