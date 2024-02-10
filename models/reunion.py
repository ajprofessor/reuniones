# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Reunion(models.Model):

    _name = 'reuniones.reunion'
    _description = 'Reuniones que se celebran en las distintas salas'

    nombre = fields.Char(required=True)
    fechaInicio = fields.Date()
    duracion = fields.Integer(string="Duración de la reunión", help="Duración en días")
    asientos = fields.Integer(string="Numero de asientos")
    asientosOcupados = fields.Float(string="Asientos ocupados", compute='_asientos_ocupados')
    sala = fields.Many2one('reuniones.sala', string="Sala de reunión", required=True, ondelete='cascade')
    responsable = fields.Many2one('res.partner', string="Responsable de la reunión", required=True)
    asistentes = fields.Many2many('res.partner', string="Asistentes a la reunión")

    @api.depends('asientos', 'asistentes')
    def _asientos_ocupados(self):
        for record in self:
            if not record.asistentos:
                record.asistentosOcupados = 0.0
            else:
                record.asistentosOcupados = 100.0 * len(record.asistentos) / record.asistentos