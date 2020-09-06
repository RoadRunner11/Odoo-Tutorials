# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom_calendar(models.Model):
    _name = 'custom_calendar.custom_calendar'
    _description = 'custom_calendar.custom_calendar'

    name = fields.Char(string='Event Name')
    start = fields.Datetime()
    end = fields.Datetime()
    duration = fields.Float( compute='_compute_duration', size=16, digits=(16, 0), required=True)

    @api.depends('start', 'end')	
    def _compute_duration(self):
        for record in self:
            record.duration = record.end -record.start
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
