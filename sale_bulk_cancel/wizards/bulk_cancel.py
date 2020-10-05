from odoo import models, fields, api


class CancelOrders(models.Model):
     _name = 'cancel.orders'
     _description = 'Cancel checked orders'

     def cancel(self):
          print("hello")
          active_ids = self._context.get('active_ids', []) or []
          for record in self.env['sale.order'].browse(active_ids):
               record.state = "cancel"