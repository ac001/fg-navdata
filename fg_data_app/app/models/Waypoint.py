# -*- coding: utf-8 -*-

from google.appengine.ext import db
import search

class Waypoint(Searchable, db.Model):
	ident = db.StringProperty(required=True, indexed=True)
	lat = db.FloatProperty(required=True)
	lng = db.FloatProperty(required=True)



