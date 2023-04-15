defaults = {}

if node.has_bundle("apt"):
    defaults['apt'] = {
        'packages': {
            'proftpd-basic': {'installed': True, },
        }
    }


@metadata_reactor
def add_ports_to_iptables(metadata):
    if not node.has_bundle('iptables'):
        raise DoNotRunAgain

    rules = {}

    rules += repo.libs.iptables.accept().chain('INPUT').tcp().\
        dest_port(metadata.get('proftp', {}).get('port', 21))
    rules += repo.libs.iptables.accept().chain('INPUT').tcp().\
        dest_port_range(*metadata.get('proftp', {}).get('passive_ports', (49152, 49252)))

    return rules
