#!/usr/bin/env python
import snmpd_pass_thru

oid_details={
	'.1.3.6.1.4.1.12345.1.2.1': {
		'exec': 'cat /etc/redhat-release',
		'type': 'String'
	},
	'.1.3.6.1.4.1.12345.1.2.2': {
		'exec': 'cat /etc/redhat-release',
		'type': 'Integer',
		'func': lambda x: int(x=='Fedora release 22 (Twenty Two)')
	},
}

snmpd_pass_thru.execute(oid_details)
