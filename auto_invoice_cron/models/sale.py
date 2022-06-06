# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class sale_order(models.Model):
    _inherit = 'sale.order'

    @api.model
    def _cron_auto_invoice_orders(self):
        #create invoices
        for so in self.env['sale.order'].search([('invoice_status', '=', 'to invoice')]):
            so._create_invoices()
