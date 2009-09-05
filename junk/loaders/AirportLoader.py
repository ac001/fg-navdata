# -*- coding: utf-8 -*-

from google.appengine.ext import db
from google.appengine.tools import bulkloader

from models.Aiports import Airport



class AirportLoader(bulkloader.Loader):

	def __init__(self):
		bulkloader.Loader.__init__(	self, 'Airport', [
								('icao', str),
                                ('name', str),
                                ('heliport', bool),
                                ('seaport', bool),
								('elevation', int),
								('atc', bool)
                               ])

class WaypointLoader(bulkloader.Loader):

	def __init__(self):
		bulkloader.Loader.__init__(	self, 'Waypint', [
								('ident', str),
                                ('lat', str),
                                ('lng', str)
                               ])
loaders = [AirportLoader]