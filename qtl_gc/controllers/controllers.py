# -*- coding: utf-8 -*-
# from odoo import http


# class QtlGc(http.Controller):
#     @http.route('/qtl_gc/qtl_gc', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/qtl_gc/qtl_gc/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('qtl_gc.listing', {
#             'root': '/qtl_gc/qtl_gc',
#             'objects': http.request.env['qtl_gc.qtl_gc'].search([]),
#         })

#     @http.route('/qtl_gc/qtl_gc/objects/<model("qtl_gc.qtl_gc"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('qtl_gc.object', {
#             'object': obj
#         })
