{
    'name': 'Partner vCard QR Code',
    'version': '18.0.1.0.0',
    'category': 'Contact',
    'summary': 'Generate QR code for partner vCard',
    'description': 'Partner vCard QR Code\n\nThis module automatically generates QR codes for partners/contacts in vCard format.\n\nFeatures:\n- Automatic QR code generation for each partner\n- Complete vCard 3.0 format support\n- Includes name, phone, email, address, position, and website\n- Easy contact import by scanning QR code with mobile phone\n- Integrated into existing partner form\n\nUsage:\n1. Open any partner/contact in Odoo\n2. Go to "QR vCard" tab\n3. Scan the QR code with mobile phone to import contact\n\nAuthor: Jiří Vysloužil\nEmail: jiri.vyslouzil2@gmail.com',
    'author': 'Jiří Vysloužil',
    'website': 'https://github.com/jirivyslouzil',
    'depends': ['base', 'contacts'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
