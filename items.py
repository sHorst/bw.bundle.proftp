
files = {}

proftp_config = node.metadata.get('proftp', {})

welcome_msg = [
    'Welcome to {hostname}'.format(hostname=node.hostname),
]

files['/etc/proftpd/welcome.msg'] = {
    'content': '\n'.join(welcome_msg) + '\n',
    'owner': 'root',
    'group': 'root',
    'mode': '0644',
}

# TODO: generate the certificates with let's encrypt
files['/etc/proftpd/tls.conf'] = {
    'owner': 'root',
    'group': 'root',
    'content_type': 'mako',
    'mode': '0644',
    'context': {
        'TLSRSACertificateFile': proftp_config.get('tls_certificate', '/etc/ssl/certs/proftpd.crt'),
        'TLSRSACertificateKeyFile': proftp_config.get('tls_privace_key', '/etc/ssl/private/proftpd.key'),
    },
    'triggers': ['svc_systemd:proftpd.service:restart', ],
}

files['/etc/proftpd/proftpd.conf'] = {
    'owner': 'root',
    'group': 'root',
    'content_type': 'mako',
    'mode': '0644',
    'context': {
        'DefaultRoot': proftp_config.get('default_root', '~/web/htdocs'),
        'Port': proftp_config.get('port', 21),
        'PassivePorts': proftp_config.get('passive_ports', (49152, 49252)),
    },
    'triggers': ['svc_systemd:proftpd.service:restart', ],
}

files['/etc/proftpd/modules.conf'] = {
    'owner': 'root',
    'group': 'root',
    'content_type': 'mako',
    'mode': '0644',
    'context': {
    },
    'triggers': ['svc_systemd:proftpd.service:restart', ],
}

files['/etc/proftpd/sql.conf'] = {
    'owner': 'root',
    'group': 'root',
    'content_type': 'mako',
    'mode': '0600',
    'context': {
    },
    'triggers': ['svc_systemd:proftpd.service:restart', ],
}


svc_systemd['proftpd.service'] = {'needs': ['pkg_apt:proftpd-basic', ], }
