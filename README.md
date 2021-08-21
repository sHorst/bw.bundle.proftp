# bw.bundle.proftp


## default config
```python
metadata= {
    'proftp': {
        'tls_certificate': '/etc/ssl/certs/proftpd.crt',
        'tls_private_key': '/etc/ssl/private/proftpd.key',

        'default_root': '~/web/htdocs',
        # 'port': 21,
        # 'passive_ports': (49152, 49252),
    },
}
```