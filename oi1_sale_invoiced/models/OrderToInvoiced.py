from odoo import models, fields, api
from odoo.exceptions import except_orm, ValidationError

from odoo import exceptions
from odoo import _

class oi1_ordertoinvoiced_wizard(models.TransientModel):    
    
    _name = 'oi1_sale_invoiced.oi1_ordertoinvoiced_wizard'
    _description = 'Set sales order to invoiced wizard'
       
    order_id    = fields.Many2one('sale.order',string='sales order', readonly="True")
    reason      = fields.Char(string='reason');
        
    @api.multi 
    def do_set_to_invoiced(self):        
        order_id = self.order_id;        
        if order_id.invoice_status != 'to invoice': 
            raise exceptions.Warning(_("This wizard will only work on salesorder with the state to invoice."));        
        for sale_order_line in order_id.order_line: 
            if len(sale_order_line.invoice_lines) == 0: 
               raise exceptions.Warning(_("This wizard will only work when every saleorderline has a least one invoice"));      
        order_id.message_post(body=_(("Sales order is manual set to invoiced Reason %s ") % self.reason))       
        order_id.invoice_status ='invoiced';
           
        
       
                    
                    
                
           
    
    
               
    
