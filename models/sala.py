# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Sala(models.Model):

    _name = 'reuniones.sala'
    _description = 'Salas disponibles para realizar reuniones'

    nombre = fields.Char(string='Sala', required=True)
    descripcion = fields.Text()
    reuniones = fields.One2many('reuniones.reunion', 'sala', string='Reuniones')