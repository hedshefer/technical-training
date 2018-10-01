from odoo import api, fields, models

class Book(models.Model):
    _name = 'library.book'
    
    name = fields.Char(string='Name')
    author_ids = fields.Many2many('library.contact', string='author')
    editor_id = fields.Many2one('library.contact', string='editor')
    edition_date = fields.Date(string='year of edition')
    isbn = fields.Char(string='ISBN')
    description = fields.Text(string="Description")
    rental_ids = fields.One2many('library.rental', 'book_id', string='rental')
    
class Rentals(models.Model):
    _name = 'library.rental'
    
    customer_id = fields.Many2one('library.contact', string='Customer')
    book_id = fields.Many2one('library.book', string='Book')

class Contact(models.Model):
    _name = 'library.contact'
    
    name = fields.Char(string='Name')