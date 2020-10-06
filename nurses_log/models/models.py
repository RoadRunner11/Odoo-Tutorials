# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class NursesLog(models.Model):
    _inherit = 'sale.order.line'

    nurse = fields.Many2one(string='Nurse/Doctor', related='order_id.partner_id')
    completed = fields.Boolean(string='Completed', default=False)
    updated_at = fields.Datetime(string='Updated At')
    is_editable = fields.Boolean(string='Is Editable', compute='_compute_is_editable', default=True)

    @api.onchange('completed')
    def _compute_completed(self):
        if self.is_editable:
            if self.nurse:
                if self.nurse != self.env.user and not self.env.user.has_group('nurses_log.group_nurse_log_doctor'):
                    raise ValueError('Sorry you are not permitted to change this.')
            else:
                self.nurse = self.env.user
            self.updated_at = datetime.now()
        else:
            return

    @api.depends('updated_at')
    def _compute_is_editable(self):
        time_diff = datetime.now() - self.updated_at
        if time_diff.days == 0 and time_diff.total_seconds() < 24 * 3600:
            self.is_editable = True
        else:
            self.is_editable = False
