# -*- coding: utf-8 -*-
# from odoo import http


# class SaleBulkCancel(http.Controller):
#     @http.route('/sale_bulk_cancel/sale_bulk_cancel/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_bulk_cancel/sale_bulk_cancel/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_bulk_cancel.listing', {
#             'root': '/sale_bulk_cancel/sale_bulk_cancel',
#             'objects': http.request.env['sale_bulk_cancel.sale_bulk_cancel'].search([]),
#         })

#     @http.route('/sale_bulk_cancel/sale_bulk_cancel/objects/<model("sale_bulk_cancel.sale_bulk_cancel"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_bulk_cancel.object', {
#             'object': obj
#         })
