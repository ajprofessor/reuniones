# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError


class Reunion(models.Model):
    _name = 'reuniones.reunion'
    _description = 'Reuniones que se celebran en las distintas salas'
    _rec_name = 'nombre'

    nombre = fields.Char(required=True)
    fechaInicio = fields.Date(default=fields.Date.today)
    fechaFin = fields.Date(string='Fecha de fin', compute='_getFechaFin', inverse='_setFechaFin', store=True)
    duracion = fields.Integer(string="Duración de la reunión", help="Duración en días")
    asientos = fields.Integer(string="Numero de asientos")
    asientosOcupados = fields.Float(string="Asientos ocupados", compute='_asientos_ocupados')
    activa = fields.Boolean(default=True)
    sala = fields.Many2one('reuniones.sala', string="Sala de reunión", required=True, ondelete='cascade')
    responsable = fields.Many2one('res.partner', string="Responsable de la reunión", required=True)
    asistentes = fields.Many2many('res.partner', string="Asistentes a la reunión")

    @api.depends('asientos', 'asistentes')
    def _asientos_ocupados(self):
        for record in self:
            if not record.asientos:
                record.asientosOcupados = 0.0
            else:
                record.asientosOcupados = 100.0 * len(record.asistentes) / record.asientos

    @api.depends('fechaInicio', 'duracion')
    def _getFechaFin(self):
        for r in self:
            if not (r.fechaInicio and r.duracion):
                continue
            fechaInicio = fields.Datetime.from_string(r.fechaInicio)
            duracion = timedelta(days=r.duracion, seconds=-1)
            r.fechaFin = fechaInicio + duracion

    def _setFechaFin(self):
        for r in self:
            if not (r.fechaInicio and r.fechaFin):
                continue
            fechaInicio = fields.Datetime.from_string(r.fechaInicio)
            fechaFin = fields.Datetime.from_string(r.fechaFin)
            r.duracion = (fechaFin - fechaInicio).days + 1

    @api.onchange('asientos', 'asistentes')
    def _validacion_asientos(self):
        if self.asientos < 0:
            return {
                'warning': {
                    'title': "Número de asientos incorrectos",
                    'message': "El número de asientos no puede ser negativo"
                }
            }
        if self.asientos < len(self.asistentes):
            return {
                'warning': {
                    'title': "Demasiados asistentes",
                    'message': "El número de asistentes supera el número de asientos"
                }
            }

    @api.constrains('responsable', 'asistentes')
    def _comprobar_responsable(self):
        for r in self.asistentes:
            if self.responsable == r:
                raise ValidationError("El responsable aparece como asistente a la reunión")
