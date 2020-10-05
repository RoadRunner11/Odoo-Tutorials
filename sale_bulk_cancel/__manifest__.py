# -*- coding: utf-8 -*-
{
    'name': "sale_bulk_cancel",

    'summary': """
        Cancel multiple orders""",

    'description': """
        The salebulk_cancel application will allow us to cancel all
        checked order at the click of a button
        
            """,

    'author': "AKOREDE FODILU OLAWALE",
    'website': "http://46.101.249.182:8069",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
