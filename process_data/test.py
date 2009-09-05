# -*- coding: utf-8 -*-


import os

import yaml
import json

"""
path="C:\\somedirectory"  # insert the path to the directory of interest
here
dirList=os.listdir(path)
for fname in dirList:
    print fname
"""
"""
dic = {'info': "blah", 'wp': [{'foo': 'bar'}]}
jj = json.dumps(dic)
print jj

js = '{info:"600 Version - data cycle 2"}'
#print json.loads(js)
"""

def file_contents(file_path):
	f = open(file_path)
	s = f.read()
	f.close()
	return s

f_types = []
f_types.append('js')
f_types.append('yaml')

for f_type in f_types:
	path = "../fg_data_app/%s" % f_type
	dirList=os.listdir(path)
	for fname in dirList:
		
		file_path = "%s/%s" % (path, fname)
		print "-----------------------------------------"
		print file_path
		print "-----------------------------------------"
		file_string = file_contents(file_path)
		if f_type == 'yaml':
			foo = yaml.load(file_string)
		elif f_type == 'js':
			#print file_string
			foo = json.loads(file_string)	

		print foo