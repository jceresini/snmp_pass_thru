#!/usr/bin/env python
import sys,os

# Function to calculate the value to return for a given oid
def calc_oid_value(oid_info):
	cmd_output = os.popen(oid_info['exec']).read().replace('\n',' ').strip()
	if 'func' in oid_info:
		value = oid_info['func'](cmd_output)
	else:
		value = cmd_output
	return value


# Function to support sorting oids
def cmp_oids(oid1,oid2):
	arr1 = oid1.split('.')
	arr2 = oid2.split('.')
	num_items = min(len(arr1),len(arr2))
	for i in range(0,num_items):
		num1=arr1[i]
		num2=arr2[i]
		if num1 > num2:
			return 1
		elif num1 < num2:
			return -1
	# If we make it this far, theyre either the same, or one has more pieces
	if len(arr1) > len(arr2):
		return 1
	elif len(arr2) > len(arr1):
		return -1
	else:
		return 0
# Function to handle snmpget/walk requests
def execute(oid_details):

	# Sort all oids this script knows how to handle
	oid_list = oid_details.keys()
	oid_list.sort(cmp_oids)

	requested_oid=sys.argv[2]

	# if its an snmpget, see if we know that oid
	if sys.argv[1] == '-g':
		if requested_oid in oid_details:
			oid_to_return=requested_oid
		else:
			oid_to_return=None

	if sys.argv[1] == '-n':
		if requested_oid not in oid_list:
			oid_list.append(requested_oid)
			oid_list.sort(cmp_oids)
	
		next_index = oid_list.index(requested_oid) + 1
		if next_index < len(oid_list):
			next_oid=oid_list[next_index]
			oid_to_return=next_oid
		else:
			oid_to_return=None

	if oid_to_return:
		print oid_to_return
		print oid_details[oid_to_return]['type']
		print calc_oid_value(oid_details[oid_to_return])
