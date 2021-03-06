# -*- coding: utf-8 -*-


class Airport(db.Model):
	icao = db.StringProperty()
	name = db.StringProperty()
	heliport = db.BooleanProperty()
	seaport = db.BooleanProperty()
	elevation = db.IntegerProperty()
	atc = db.BooleanProperty()


class RunwayTaxi(db.Model):
	airport = db.ReferenceProperty(Airport)
	type = db.StringProperty()
	num = db.StringProperty()
	geo = db.GeoPtProperty()
	abslng = db.FloatProperty()
	heading = db.FloatProperty()
	length = db.IntegerProperty()
	width = db.IntegerProperty()

