# -*- coding: utf-8 -*-

import json

data = json.load(open("../fg_data_app/js/waypoints.snall.js", 'r'))

print "loaded"
print data.keys()

import urllib
import urllib2

url = 'http://localhost:8888/foo'


batch = []
for w in data['waypoints']:
	print w
	values = {'set' : 'waypoint', 'data': w}
	data = urllib.urlencode(values)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	the_page = response.read()
	print the_page
	print "--------------------------------------------"
	#if len(w) == 100:
	#	print batch
	#	break