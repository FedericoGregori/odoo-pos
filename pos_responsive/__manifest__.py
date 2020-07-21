# -*- coding: utf-8 -*-
{
    'name': "Responsive for PoS",

    'summary': "Mobile view for PoS screen.",

    'author': "Federico Gregori",
    'license': "AGPL-3",
    'website': "www.federicogregori.com",
    'category': 'PoS',
    'version': '13.0.0.1',
    'depends': ['point_of_sale', 'pos_restaurant'],
    'qweb': ['static/src/xml/pos.xml'],
    'data': ['views/pos_responsive.xml'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
