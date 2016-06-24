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
    'ramrojob': {}
}
