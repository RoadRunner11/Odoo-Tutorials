# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tutorials(models.Model):
     _name = 'tutorials.tutorials'
     _description = 'tutorials.tutorials'

     title = fields.Char()
     content = fields.Html()
     author = fields.Many2one("res.partner", string="author")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
