# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class client_history_product(models.Model):
#     _name = 'client_history_product.client_history_product'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100