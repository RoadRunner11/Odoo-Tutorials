from odoo import models, fields, api


class CancelOrders(models.TransientModel):
     _name = 'cancel.orders'
     _description = 'Cancel checked orders'

     @api.multi
     def sale_bulk_cancel(self):
          print("hello")