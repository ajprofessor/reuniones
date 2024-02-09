# -*- coding: utf-8 -*-
# from odoo import http


# class /mnt/extra-addons/reuniones(http.Controller):
#     @http.route('//mnt/extra-addons/reuniones//mnt/extra-addons/reuniones', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//mnt/extra-addons/reuniones//mnt/extra-addons/reuniones/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('/mnt/extra-addons/reuniones.listing', {
#             'root': '//mnt/extra-addons/reuniones//mnt/extra-addons/reuniones',
#             'objects': http.request.env['/mnt/extra-addons/reuniones./mnt/extra-addons/reuniones'].search([]),
#         })

#     @http.route('//mnt/extra-addons/reuniones//mnt/extra-addons/reuniones/objects/<model("/mnt/extra-addons/reuniones./mnt/extra-addons/reuniones"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/mnt/extra-addons/reuniones.object', {
#             'object': obj
#         })
