# -*- coding: utf-8 -*-

from google.appengine.ext import db

# http://www.billkatz.com/2009/6/Simple-Full-Text-Search-for-App-Engine
from search import Searchable

class Waypoint(Searchable, db.Model):
	ident = db.StringProperty(required=True, indexed=True)
	lat = db.FloatProperty(required=True)
	lng = db.FloatProperty(required=True)
	INDEX_ONLY = ['ident']
	INDEX_TITLE_FROM_PROP = 'ident'  

