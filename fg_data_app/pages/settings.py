# -*- coding: utf-8 -*-

import os

pages = [('/', 'Index'), ('/waypoints', 'Waypoints')] #, ('/airports', 'Airports')]

file_types =  ['js', 'yaml']

app = {'title': "Flight Gear / xPlane - data cloud (experimental)", 'version': os.environ['CURRENT_VERSION_ID']}

root_path = os.path.abspath(os.path.dirname(__file__) + "/../")

links = ['https://appengine.google.com/']
