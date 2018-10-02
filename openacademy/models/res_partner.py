from odoo import models, fields, api

class Partner(models.Model):
    _inherit = "res.partner"
    
    is_instructor = fields.Boolean("instructor", default=False)