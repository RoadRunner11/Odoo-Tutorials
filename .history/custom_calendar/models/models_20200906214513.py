# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

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
            d1=datetime.strptime(str(self.from_date),'%Y-%m-%d') 
            d2=datetime.strptime(str(self.final_date),'%Y-%m-%d')
            d3=d2-d1
            record.duration = str(d3.days)
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100