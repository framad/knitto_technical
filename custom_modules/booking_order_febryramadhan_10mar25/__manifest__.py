# -*- coding: utf-8 -*-
{
    'name': "Booking Order Febry Ramadhan",

    'summary': """
        Module Booking Order Febry Ramadhan""",

    'description': """
        Module ujian booking order Febry Ramadhan knitto
    """,

    'author': "Febry Ramadhan",
    'website': "https://framad.github.io/framadhan",

    'category': 'Uncategorized',
    'version': '0.1',

		# Depencicy
    'depends': ['base','sale'],

		# Include ALL XML Code in Here be mindful of order
    'data': [
        'security/ir.model.access.csv',
        'views/canceled_order.views.xml',
        'views/work_order.views.xml',
        'views/booking_order.views.xml',
        'views/service_team.views.xml',
        'views/menuitems.views.xml',
        'report/report_work_order.xml',
        'report/report.xml',
        'data/data.xml'
    ],

    'installable': True,
    'application': True,
    'auto_install': False

}