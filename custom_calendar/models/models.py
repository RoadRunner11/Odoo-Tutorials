# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class custom_calendar(models.Model):
    _name = 'custom_calendar.custom_calendar'
    _description = 'custom_calendar.custom_calendar'

    name = fields.Char(string='Event Name')
    start = fields.Datetime(string="Start date")
    end = fields.Datetime(string="End date")
    duration = fields.Integer(  string=" Duration")

    @api.onchange('start', 'end', 'duration')
    def calculate_date(self):
        if self.start and self.end:
            d1=datetime.strptime(str(self.start),'%Y-%m-%d %H:%M:%S') 
            d2=datetime.strptime(str(self.end),'%Y-%m-%d %H:%M:%S')
            d3=d2-d1
            self.duration=str(d3.days)
    # @api.depends('start', 'end')	
    # def _compute_duration(self):
    #     for record in self:
    #         d1=datetime.strptime(str(self.start), "%Y-%m-%d %H:%M:%S")
    #         d2=datetime.strptime(str(self.end), "%Y-%m-%d %H:%M:%S")
    #         d3=d2-d1
    #         self.duration = abs(d3.days)
