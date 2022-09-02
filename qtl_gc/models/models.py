# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class qtl_gc(models.Model):
#     _name = 'qtl_gc.qtl_gc'
#     _description = 'qtl_gc.qtl_gc'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
