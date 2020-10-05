# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CancelOrders(models.TransientModel):
    _name = 'cancel.orders'
    _description = 'Cancel checked orders'

    def cancel(self):
        active_ids = self._context.get('active_ids', []) or []
        for record in self.env['sale.order'].browse(active_ids):
            record.state = "Cancelled"
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
