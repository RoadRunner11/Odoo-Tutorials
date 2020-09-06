# -*- coding: utf-8 -*-
# from odoo import http


# class CustomCalendar(http.Controller):
#     @http.route('/custom_calendar/custom_calendar/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_calendar/custom_calendar/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_calendar.listing', {
#             'root': '/custom_calendar/custom_calendar',
#             'objects': http.request.env['custom_calendar.custom_calendar'].search([]),
#         })

#     @http.route('/custom_calendar/custom_calendar/objects/<model("custom_calendar.custom_calendar"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_calendar.object', {
#             'object': obj
#         })
