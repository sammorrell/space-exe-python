# This is to show you how to use dictionaries. 
# They contain key value pairs of Python objects.
dict_1 = { 'number_property' : 1953.452, 'text_property' : 'Value' }
dict_2 = {
	'name' : 'V* LM Tau',
	'ra' : 55.5417,
	'dec' : 24.0856,
	'spectral-type' : 'M',
	'variable' : True
}

# Indiviual elements within dictionaries can be access like so
star_name = dict_2['name']
variable_star = dict_2['variable']

# And they can be set like so
dict_2['variable'] = False
dict_2['name'] = 'LM Tau'