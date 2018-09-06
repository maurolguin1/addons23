# -*- coding: utf-8 -*-
# Part of eComBucket. See LICENSE file for full copyright and licensing details
from . import models
def odoo_version_check(cr):
    from openerp.exceptions import Warning
    from openerp.service import common
    exp_version = common.exp_version()

    return True
