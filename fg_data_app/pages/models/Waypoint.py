# -*- coding: utf-8 -*-

from google.appengine.ext import db

class Waypoint(db.Model):
	ident = db.StringProperty()
	geo = db.GeoPtProperty()



