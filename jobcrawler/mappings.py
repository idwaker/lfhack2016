# -*- coding: utf-8 -*-


_DISTRICTS = (
    'Taplejung', 'Panchthar', 'Ilam', 'Jhapa', 'Morang', 'Sunsari', 'Dhankuta',
    'Terhathum', 'Sankhuwasabha', 'Bhojpur', 'Solukhumbu', 'Okhaldhunga', 'Khotang',
    'Udayapur', 'Saptari', 'Siraha', 'Dhanusa', 'Mahottari', 'Sarlahi', 'Sindhuli',
    'Ramechhap', 'Dolakha', 'Sindhupalchok', 'Kavrepalanchok', 'Lalitpur', 'Bhaktapur',
    'Kathmandu', 'Nuwakot', 'Rasuwa', 'Dhading', 'Makwanpur', 'Rautahat', 'Bara',
    'Parsa', 'Chitawan', 'Gorkha', 'Lamjung', 'Tanahu', 'Syangja', 'Kaski', 'Manang',
    'Mustang', 'Myagdi', 'Parbat', 'Baglung', 'Gulmi', 'Palpa', 'Nawalparasi',
    'Rupandehi', 'Kapilbastu', 'Arghakhanchi', 'Pyuthan', 'Rolpa', 'Rukum', 'Salyan',
    'Dang', 'Banke', 'Bardiya', 'Surkhet', 'Dailekh', 'Jajarkot', 'Dolpa', 'Jumla',
    'Kalikot', 'Mugu', 'Humla', 'Bajura', 'Bajhang', 'Achham', 'Doti', 'Kailali',
    'Kanchanpur', 'Dadeldhura', 'Baitadi', 'Darchula'
)

DISTRICTS = (d.lower() for d in _DISTRICTS)

INDUSTRY_FILTERS = {
    'merojob': {
        'Bank, Finance & Insurance': ('Banks', 'Finance Companies', 
                                      'Insurance Companies'),
        'IT, Software & Telecommunication': (
            'Information / Computer / Technology', 'Software Companies',
            'Hardware / Network Companies', 'ISP', 'Telecommunication',                                     
        ),
    },
    'ramrojob': {
        'Bank, Finance & Insurance': ('Bank', 'Insurance', 'Finance Company',
                                      'Investment Company', 'Remittance',
                                      'Accounting / Audit'),
        'IT, Software & Telecommunication': ('Information Technology / Software',
                                             'Telecommunication', 'E-commerce / Online Store')
    }
}

CATEGORY_FILTERS = {
    'merojob': {
        'Accounting': ('Accounting / Finance',),
        'Banking / Insurance /Financial Services': ('Banking / Insurance /Financial Services'),
        'Human Resource': (' Human Resource /Org. Development',),
        'Administration & Operation': ('General Mgmt. / Administration / Operations',),
        'Legal Services': ('Legal Services',),
        'Telecommunication': ('Filter by telecommunication in  IT & Telecommunication',),
        'Software Development': ('Creative / Graphics / Designing',
                                 'All except telecommunication in  IT & Telecommunication'),
        'Secretarial / Front Office / Data Entry': ('Secretarial / Front Office / Data Entry',),
        'Marketing / Advertising / Customer Service': ('Marketing / Advertising / Customer Service',),
        'Sales / Distribution / Public Relations': ('Sales / Public Relations',),
    },
    'ramrojob': {
        'Accounting': ('Accounting',),
        'Banking / Insurance /Financial Services': ('Banking / Financial Services', 'Insurance'),
        'Human Resource': ('Human Resource',),
        'Administration & Operation': ('Finance / Administration', 'Management / Operations',
                                       'Purchasing / Procurement'),
        'Legal Services': ('Legal Services',),
        'Telecommunication': ('Telecommunication',),
        'Software Development': ('Cloud Computing', 'IT / Database Management', 
                                 'IT / Software', 'Programming / Graphics / Designing',
                                 'Search Engine Optimization (SEO)'),
        'Secretarial / Front Office / Data Entry': ('Computer Operator', 
                                                    'Customer Service / Data Entry',
                                                    'Secretary',),
        'Marketing / Advertising / Customer Service': ('Marketing / Advertising', 
                                                       'Customer Service'),
        'Sales / Distribution / Public Relations': ('Sales / Distribution',
                                                    'Public Relation', 'Business Development'),
    }
}
