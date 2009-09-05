# -*- coding: utf-8 -*-

import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.ext import db

import settings

from models.Waypoint import Waypoint


class FooPage(webapp.RequestHandler):

	def post(self):
		self.response.out.write("OK")


	def get(self):

		## check werre not creating dupes
		
		#query = db.GqlQuery("select * from Waypoint where ident=:1", XX)
		#existing_waypoints = query.fetch(limit=1)
		## not exist so create
		#way = Waypoint.get_or_insert(key_name=XX, ident=XX, lat=2.3, lng=6.3338)
		#way.put()
		
		#self.response.out.write("OK get")

		#return
		XX = "XssssX"
		way = Waypoint.get_by_key_name(XX)
		if way:
			way.lat = -10.0
			way.lng = 9349.99
			way.put()
		else:
			way = Waypoint(key_name=XX, ident=XX, lat=2.3, lng=6.8)
			way.put()
			
		self.response.out.write("OK get")

		return
		template_vars = {}
		#template_vars['app'] = {'title': 'FG-Data-Developement version', 'version': '0.1-Alpha'}
		template_vars['settings'] = settings
		template_vars['files'] = ['foo']

		path = settings.templates_path + '/foo.html'

		self.response.out.write(template.render(path, template_vars))