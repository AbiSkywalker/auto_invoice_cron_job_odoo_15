# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
import logging
_logger = logging.getLogger(__name__)

class sale_order(models.Model):
    _inherit = 'sale.order'

    @api.model
    def _cron_auto_invoice_orders(self):
        _logger.info("RUNNING AUTO INVOICE")
        #crear facturas
        for so in self.env['sale.order'].search([('invoice_status', '=', 'to invoice')]):
            so._create_invoices()