# -*- coding: utf-8 -*-
{
    'name': "oi1_partner_parentcompany",
    'summary': """
        This module will add the option to have a company with different branches
        """,
    'author': "OntwikkelingInEenvoud (Remko Strating)",
    'website': "http://www.oi1.nl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Partner',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',      
        'views/res_partner.xml',         
        ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
