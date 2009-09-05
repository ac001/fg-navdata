# -*- coding: utf-8 -*-

from google.appengine.ext import db

class Airport(db.Model):
	icao = db.StringProperty()
	name = db.StringProperty()
	heliport = db.BooleanProperty()
	seaport = db.BooleanProperty()
	elevation = db.IntegerProperty()
	atc = db.BooleanProperty()




