# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Thực Tập',
    'version': '0.1',
    'sequence': 5,
    'category': 'Productivity',
    'website': 'google.com',
    'summary': 'Bán độ đua xe',
    'description': """
Bla bla bla... 
""",
    'depends': [],
    'data': [
        'views/bidding_package.xml',
        'views/size_standard.xml',
        'data/sequence_bidding_package.xml',
        'data/sequence_size_standard.xml'
    ],
    'installable': True,
    'application': True,
}
