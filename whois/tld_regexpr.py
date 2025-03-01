com = {
    'extend': None,

    'domain_name':				r'Domain Name:\s?(.+)',
    'registrar':				r'Registrar:\s?(.+)',
    'registrant':				None,

    'creation_date':			r'Creation Date:\s?(.+)',
    'expiration_date':			r'Registry Expiry Date:\s?(.+)',
    'updated_date':				r'Updated Date:\s?(.+)$',

    'name_servers':				r'Name Server:\s*(.+)\s*',
    'status':					r'Status:\s?(.+)',
    'emails':					r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

net = {
    'extend': 'com',
}

org = {
    'extend': 'com',

    'expiration_date':			r'\nRegistry Expiry Date:\s?(.+)',
    'updated_date':				r'\nLast Updated On:\s?(.+)',

    'name_servers':				r'Name Server:\s?(.+)\s*',
}

uk = {
    'extend': 'com',

    'registrant':				r'Registrant:\n\s*(.+)',

    'creation_date':			r'Registered on:\s*(.+)',
    'expiration_date':			r'Renewal date:\s*(.+)',
    'updated_date':				r'Last updated:\s*(.+)',

    'name_servers':				r'Name Servers:\s*(.+)\s*',
    'status':					r'Registration status:\n\s*(.+)',
}

pl = {
    'extend': 'uk',

    'creation_date':			r'\ncreated:\s*(.+)\n',
    'updated_date':				r'\nlast modified:\s*(.+)\n',

    'name_servers':				r'\nnameservers:\s*(.+)\n\s*(.+)\n',
    'status':					r'\nStatus:\n\s*(.+)',
}

ru = {
    'extend': 'com',

    'domain_name':				r'\ndomain:\s*(.+)',

    'creation_date':			r'\ncreated:\s*(.+)',
    'expiration_date':			r'\npaid-till:\s*(.+)',

    'name_servers':				r'\nnserver:\s*(.+)',
    'status':					r'\nstate:\s*(.+)',
}

ru_rf = {
    'extend': 'com',

    'domain_name':				r'\ndomain:\s*(.+)',

    'creation_date':			r'\ncreated:\s*(.+)',
    'expiration_date':			r'\npaid-till:\s*(.+)',

    'name_servers':				r'\nnserver:\s*(.+)',
    'status':					r'\nstate:\s*(.+)',
}

lv = {
    'extend': 'ru',

    'creation_date':			r'Registered:\s*(.+)\n',
    'updated_date':				r'Changed:\s*(.+)\n',

    'status':					r'Status:\s?(.+)',
}

jp = {
    'domain_name':				r'\[Domain Name\]\s?(.+)',
    'registrar':				None,
    'registrant':				r'\[Registrant\]\s?(.+)',

    'creation_date':			r'\[Created on\]\s?(.+)',
    'expiration_date':			r'\[Expires on\]\s?(.+)',
    'updated_date':				r'\[Last Updated\]\s?(.+)',

    'name_servers':				r'\[Name Server\]\s*(.+)',
    'status':					r'\[Status\]\s?(.+)',
    'emails':					r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

co_jp = {
    'extend': 'jp',

    'creation_date':			r'\[Registered Date\]\s?(.+)',
    'expiration_date':			r'\[State\].+\((.+)\)',
    'updated_date':				r'\[Last Update\]\s?(.+)',
}

de = {
    'extend': 'com',
    'domain_name':				r'\ndomain:\s*(.+)',
    'updated_date':				r'\nChanged:\s?(.+)',
    'name_servers':				r'Nserver:\s*(.+)',
}

at = {
    'extend': 'com',
    'domain_name':				r'domain:\s?(.+)',
    'updated_date':				r'changed:\s?(.+)',
    'name_servers':				r'nserver:\s*(.+)',
}

eu = {
    'extend': 'com',

    'domain_name':				r'\ndomain:\s*(.+)',
    'registrar':				r'Name:\s?(.+)',
}

biz = {
    'extend': 'com',

    'registrar':				r'Sponsoring Registrar:\s?(.+)',
    'registrant':				r'Registrant Organization:\s?(.+)',

    'creation_date':			r'Domain Registration Date:\s?(.+)',
    'expiration_date':			r'Domain Expiration Date:\s?(.+)',
    'updated_date':				r'Domain Last Updated Date:\s?(.+)',

    'status':					None,
}

info = {
    'extend': 'com'
}

name = {
    'extend': 'com',

    'status':					r'Domain Status:\s?(.+)',
}

us = {
    'extend': 'name',
}

co = {
    'extend': 'biz',

    'status':					r'Status:\s?(.+)',
}

me = {
    'extend': 'biz',

    'creation_date':			r'Domain Create Date:\s?(.+)',
    'expiration_date':			r'Domain Expiration Date:\s?(.+)',
    'updated_date':				r'Domain Last Updated Date:\s?(.+)',

    'name_servers':				r'Nameservers:\s?(.+)',
    'status':					r'Domain Status:\s?(.+)',
}

be = {
    'extend': 'pl',

    'domain_name':				r'\nDomain:\s*(.+)',
    'registrar':				r'Company Name:\n?(.+)',

    'creation_date':			r'Registered:\s*(.+)\n',

    'status':					r'Status:\s?(.+)',
}

nz = {
    'extend': None,

    'domain_name':				r'domain_name:\s?(.+)',
    'registrar':				r'registrar_name:\s?(.+)',
    'registrant':				r'registrant_contact_name:\s?(.+)',

    'creation_date':			r'domain_dateregistered:\s?(.+)',
    'expiration_date':			r'domain_datebilleduntil:\s?(.+)',
    'updated_date':				r'domain_datelastmodified:\s?(.+)',

    'name_servers':				r'ns_name_[0-9]{2}:\s?(.+)',
    'status':					r'query_status:\s?(.+)',
    'emails':					r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

cz = {
    'extend': 'com',

    'domain_name':				r'Domain:\s?(.+)',
    'registrar':				r'registrar:\s?(.+)',
    'registrant':				r'registrant:\s?(.+)',

    'creation_date':			r'registered:\s?(.+)',
    'expiration_date':			r'expire:\s?(.+)',
    'updated_date':				r'changed:\s?(.+)',

    'name_servers':				r'nserver:\s*(.+) ',
}

it = {
    'extend': 'com',

    'domain_name':				r'Domain:\s?(.+)',
    'registrar':				r'Registrar:\s*Organization:\s*(.+)',
    'registrant':				r'Registrant:\s?Name:\s?(.+)',

    'creation_date':			r'Created:\s?(.+)',
    'expiration_date':			r'Expire Date:\s?(.+)',
    'updated_date':				r'Last Update:\s?(.+)',

    'name_servers':				r'Nameservers:\s?(.+)\s?(.+)\s?(.+)\s?(.+)',
    'status':					r'Status:\s?(.+)',
}

fr = {
    'extend': 'com',

    'domain_name':				r'domain:\s?(.+)',
    'registrar':				r'registrar:\s*(.+)',
    'registrant':				r'contact:\s?(.+)',

    'creation_date':			r'created:\s?(.+)',
    'expiration_date':			None,
    'updated_date':				r'last-update:\s?(.+)',

    'name_servers':				r'nserver:\s*(.+)',
    'status':					r'status:\s?(.+)',
}

io = {
    'extend': 'com',
    'expiration_date':			r'\nRegistry Expiry Date:\s?(.+)',
}

ca = {
    'extend': 'com',

    'domain_name':				r'domain:\s?(.+)',
    'registrar':				r'registrar:\s*(.+)',
    'registrant':				r'contact:\s?(.+)',

    'creation_date':			r'created:\s?(.+)',
    'expiration_date':			None,
    'updated_date':				r'last-update:\s?(.+)',

    'name_servers':				r'nserver:\s*(.+)',
    'status':					r'status:\s?(.+)',
}

br = {
    'extend': 'com',
    'domain_name':              r'domain:\s?(.+)',
    'registrar':                'nic.br',
    'registrant':               None,
    'owner':                    r'owner:\s?(.+)',
    'creation_date':            r'created:\s?(.+)',
    'expiration_date':          r'expires:\s?(.+)',
    'updated_date':             r'changed:\s?(.+)',
    'name_servers':             r'nserver:\s*(.+)',
    'status':                   r'status:\s?(.+)',
}

mx = {
    'domain_name':              r'Domain Name:\s?(.+)',
    'registrant':               r'Registrant:\n\s*(.+)',
    'registrar':                r'Registrar:\s?(.+)',
    'creation_date':            r'Created On:\s?(.+)',
    'expiration_date':          r'Expiration Date:\s?(.+)',
    'updated_date':             r'Last Updated On:\s?(.+)',
    'name_servers':             r'\sDNS:\s*(.+)',
}

sh = {
    'extend': 'com',
    'expiration_date':         r'\nRegistry Expiry Date:\s*(.+)',
    'registrant':              r'\nRegistrant Organization:\s?(.+)',
    'status':                  r'\nDomain Status:\s?(.+)',
}

video = {
    'extend': 'com',
    'expiration_date':          r'\nRegistry Expiry Date:\s?(.+)',
    'updated_date':             r'\nUpdated Date:\s?(.+)',
}

mobi = {
    'extend': 'com',
    'expiration_date':          r'\nRegistry Expiry Date:\s?(.+)',
    'updated_date':             r'\nUpdated Date:\s?(.+)',
}

uz = {
    'extend': 'com',
    'domain_name':              r'Domain Name:\s?(.+)',
    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Expiration Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',
    'status':                   r'Status:\s?(.+)',
}

id = {
    'extend': 'com',

    'registrar':				r'Sponsoring Registrar Organization:\s?(.+)',

    'creation_date':			r'Created On:\s?(.+)',
    'expiration_date':			r'Expiration Date:\s?(.+)',
    'updated_date':				r'Last Updated On:\s?(.+)$',
}


store = {
    'extend': 'com',
    'registrar':				r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',
    'creation_date':			r'Creation Date:\s?(.+)',
    'expiration_date':			r'Registry Expiry Date:\s?(.+)',
    'name_servers':             r'Name Server:\s*(.+)',
    'status':                   r'Domain Status:\s*(.+)'
}

rest = {
    'extend': 'store',
    'status':                   r'Domain Status:\s*(.+)'
}

security = {
    'extend': 'store'
}

site = {
    'extend' : 'store'
}

website = {
    'extend' : 'store'
}

tickets = {
    'extend': 'store'
}

theatre = {
    'extend': 'store'
}

tech = {
    'extend': 'store'
}

space = {
    'extend' : 'store'
}
xyz = {
    'extend': 'com',
    'domain_name':              r'Domain Name:\s?(.+)',
    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'\nRegistry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',
    'status':                   r'Status:\s?(.+)',
}

tel = {
    'extend': 'com',
    'domain_name':              r'Domain Name:\s?(.+)',
    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'\nRegistry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',
    'status':                   r'Status:\s?(.+)',
}

tv = {
    'extend': 'com',
    'domain_name':              r'Domain Name:\s?(.+)',
    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',
    'status':                   r'Status:\s?(.+)',
}

cc = {
    'extend': 'com',
    'domain_name':              r'Domain Name:\s?(.+)',
    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',
    'status':                   r'Status:\s?(.+)',
}

nyc = {
    'extend': 'com',
    'domain_name':              r'Domain Name:\s?(.+)',
    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',
    'status':                   r'Status:\s?(.+)',
}

pw = {
    'extend': 'com',
    'domain_name':              r'Domain Name:\s?(.+)',
    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',
    'status':                   r'Status:\s?(.+)',
}

online = {
    'extend': 'com',
    'domain_name':              r'Domain Name:\s?(.+)',
    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',
    'status':                   r'Status:\s?(.+)',
}

wiki = {
    'extend': 'com',
    'domain_name':              r'Domain Name:\s?(.+)',
    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',
    'status':                   r'Status:\s?(.+)',
}

press = {
    'extend': 'com',
    'domain_name':              r'Domain Name:\s?(.+)',
    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',
    'status':                   r'Status:\s?(.+)',
}

pharmacy = {
    'extend': 'com',
    'domain_name':              r'Domain Name:\s?(.+)',
    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',
    'status':                   r'status:\s?(.+)',
}

kr = {
    'extend': 'com',
    'domain_name':              r'Domain Name\s*:\s?(.+)',
    'registrar':                r'Authorized Agency\s*:\s*(.+)',
    'registrant':				r'Registrant\s*:\s*(.+)',
    'creation_date':            r'Registered Date\s*:\s?(.+)',
    'expiration_date':          r'Expiration Date\s*:\s?(.+)',
    'updated_date':             r'Last Updated Date\s*:\s?(.+)',
    'status':                   r'status\s*:\s?(.+)',
}

cn = {
    'extend': 'com',
    'registrar':                r'Sponsoring Registrar:\s?(.+)',
    'registrant':				r'Registrant:\s?(.+)',
    'creation_date':			r'Registration Time:\s?(.+)',
    'expiration_date':			r'Expiration Time:\s?(.+)'
}
