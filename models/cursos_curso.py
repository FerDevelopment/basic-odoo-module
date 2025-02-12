

from odoo import models, fields, api

class Curso(models.Model):
    _name = 'cursos.curso'
    _description = 'Curso a programar para el aprendizaje de nuevas habilidades para el futuro'

    organizador= fields.Many2one('res.employee', string='Organizador')
    asistentes= fields.One2many('res.employee', string='Asistentes')
    titulo= fields.Char('Título', required=True)
    descripcion= fields.Char(string='Descripción')
    fechaInicio= fields.Date(string='Fecha de inicio')
    fechaFin= fields.Date(string= 'Fecha de inicio')
    activo= fields.Boolean(string= 'Activo', default=False)