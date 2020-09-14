# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class custom_calendar(models.Model):
    _name = 'custom_calendar.custom_calendar'
    _description = 'custom_calendar.custom_calendar'

    name = fields.Char(string='Event Name')
    start = fields.Date(string="Start date")
    end = fields.Date(string="End date")
    duration = fields.Float( compute='_compute_duration', required=True)

    @api.onchange('from_date', 'final_date','total_days')
    def calculate_date(self):
        if self.start and self.end:
            d1=datetime.strptime(str(self.start),'%Y-%m-%d') 
            d2=datetime.strptime(str(self.end),'%Y-%m-%d')
            d3=d2-d1
            self.duration=str(d3.days)
    # @api.depends('start', 'end')	
    # def _compute_duration(self):
    #     for record in self:
    #         d1=datetime.strptime(str(self.start), "%Y-%m-%d %H:%M:%S")
    #         d2=datetime.strptime(str(self.end), "%Y-%m-%d %H:%M:%S")
    #         d3=d2-d1
    #         self.duration = abs(d3.days)
