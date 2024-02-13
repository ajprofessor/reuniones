# -*- coding: utf-8 -*-
{
    'name': "Gestión de la sala de reuniones",

    'summary': "Módulo para la gestión de las salas de reuniones de la empresa",

    'description': """
En este módulo guardaremos la información de las salas y de las reuniones que se harán en ellas
    """,

    'author': "AJ",
    'website': "https://eldelbit.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.5',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/reunion_view.xml',
        'views/sala_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'license':  'LGPL-3'
}
