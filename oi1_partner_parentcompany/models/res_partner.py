from odoo import models, fields, api
from odoo import exceptions

class res_partner(models.Model):    
       
    _inherit  = 'res.partner'
                                 
    x_parent_company_id     = fields.Many2one('res.partner','Parent company', index=True, domain=[('is_company','=',True),('x_has_locations','=',True)])
    x_location_ids          = fields.One2many('res.partner', 'x_parent_company_id','Locations') 
    x_has_locations         = fields.Boolean(string ='Has different locations', default=False)  
    
   
  
    
    