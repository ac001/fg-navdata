# -*- coding: utf-8 -*-

import json, sys

data = json.load(open("../fg_data_app/js/waypoints.snall.js", 'r'))

print "loaded"
print data.keys()

import urllib
import urllib2

url = 'http://localhost:8888/foo'


batch = []
for w in data['waypoints']:
	batch.append(w)
	if len(batch) == 100:
		print "--------------------------------------------"
		values = {'set' : 'waypoints', 'data': json.dumps(batch)}
		print values
		data = urllib.urlencode(values)
		req = urllib2.Request(url, data)
		response = urllib2.urlopen(req)
		the_page = response.read()
		print the_page
		sys.exit(1)
		
	#if len(w) == 100:
	#	print batch
	#	break