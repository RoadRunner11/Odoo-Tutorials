# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ChangeState(models.TransientModel):
    _name = 'update.state'
    _description = 'Change the state of sale order'
    
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
    ], string = 'Status')
    def update_state(self):
        active_ids = self._context.get('active_ids', []) or []
        for record in self.env['sale.order'].browse(active_ids):
            record.state = self.state
