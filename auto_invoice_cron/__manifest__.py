# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)


{
    "name": "Auto invoice",
    "summary": "Add cron job to generate invoices automatically every week",
    "version": "1.0",
    'author': "Abi Skywalker",
    'website': "",
    'category': 'perso',
    'version': '1.0',
    'depends': ['sale','sale_management','account'],
    'data': [
        'data/cron.xml'
            ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
}