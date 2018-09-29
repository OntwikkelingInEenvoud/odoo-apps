# -*- coding: utf-8 -*-
from openerp import http

# class Ekstraitinvoicing(http.Controller):
#     @http.route('/ekstraitinvoicing/ekstraitinvoicing/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ekstraitinvoicing/ekstraitinvoicing/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ekstraitinvoicing.listing', {
#             'root': '/ekstraitinvoicing/ekstraitinvoicing',
#             'objects': http.request.env['ekstraitinvoicing.ekstraitinvoicing'].search([]),
#         })

#     @http.route('/ekstraitinvoicing/ekstraitinvoicing/objects/<model("ekstraitinvoicing.ekstraitinvoicing"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ekstraitinvoicing.object', {
#             'object': obj
#         })