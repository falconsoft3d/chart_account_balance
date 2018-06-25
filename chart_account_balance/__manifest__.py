# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO, Open Source Management Solution
#    Copyright (C) 2016 Steigend IT Solutions
#    For more details, check COPYRIGHT and LICENSE files
#
##############################################################################
{
    'name': "Balance de Cuentas MFH",
    'summary': """  Débitos, créditos y saldo de las cuentas contables""",
    'description': """
        Agrega campos calculados de débito, crédito y saldo en la vista en tree de las cuentas contables
    """,
    'author': "Falcón Solutions",
    'maintainer': 'Falcon Solutions',
    'website': 'http://www.falconsolutions.cl',
    'license': 'AGPL-3',
    'category': 'Account',
    'version': '10.0.1',
    'depends': ['account'],
    'data': [
        'views/account_view.xml',
    ],
    'demo': [
    ],
}
