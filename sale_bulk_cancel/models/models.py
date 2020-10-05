# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sale_bulk_cancel(models.TransientModel):
    _name = "bulk.cancel"
    _description = 'This allows a user to cancel all checked orders'
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
    def action_cancel(self):
        active_ids = self._context.get("active_ids", []) or []
        for record in self.env["sale.order"].browse(active_ids):
            record.state = "Cancelled"

