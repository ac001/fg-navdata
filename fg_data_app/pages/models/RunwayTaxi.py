# -*- coding: utf-8 -*-

from google.appengine.ext import db

import Airport

class RunwayTaxi(db.Model):
	airport = db.ReferenceProperty(Airport.Airport)
	type = db.StringProperty()
	num = db.StringProperty()
	geo = db.GeoPtProperty()
	abslng = db.FloatProperty()
	heading = db.FloatProperty()
	length = db.IntegerProperty()
	width = db.IntegerProperty()




