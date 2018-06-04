# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class client_history_product(models.Model):
    _inherit = 'res.partner'

    list_products = fields.Many2many(
        'product.template', compute='_get_last_10_product')

    def _get_last_10_product(self):
        for partner in self:
            products = []
            order_ids = self.env['pos.order'].search([
                ('partner_id', '=', partner.id)
            ])
            for order in order_ids:
                if order:
                    for line in order.lines:
                        if not line.product_id in products:
                            products.append(line.product_id.product_tmpl_id.id)
                            if len(products) > 10:
                                partner.list_products = products
                                return

            partner.list_products = products



class PosOrderLine(models.Model):
    _inherit = 'pos.order.line'

    partner_id = fields.Many2one('pos.order', 'partner_id')
