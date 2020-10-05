# -*- coding: utf-8 -*-
{
    'name': "sale_bulk_cancel",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        The Tutorials application will help us keep proper
        records of our works. This means we can store our
        tasks and the tutorials attached to these tasks in this 
        Tutorials application. By doing this, we can make sure 
            that we are losing out any important 
        information relating to works, both internal and external works.
        """ ,

    'author': "AKOREDE FODILU OLAWALE",
    'website': "http://46.101.249.182:8069",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ["base"],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
