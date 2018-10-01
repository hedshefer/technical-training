from odoo import api, fields, models

class Course(models.Model):
    _name = 'openacademy.course'
    
    name = fields.Char(string='Name')
    description = fields.Text(string="Description")
    responsible_id = fields.Many2one('res.partner', string='Responsible')