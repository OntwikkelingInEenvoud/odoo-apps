# -*- coding: utf-8 -*-
{
    'name': "oi1_sale_invoiced",

    'summary': """
        This module will set the salesorders to invoiced.  
        """,    
    'author': "OntwikkelingInEenvoud (Remko Strating)",
    'website': "http://www.oi1.nl",
    'category': 'Sale',
    'version': '0.2',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        'views/OrderToInvoiced.xml'
      
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
