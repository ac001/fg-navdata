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


		set_item = self.request.get("set")
		data = json.loads(self.request.get('data'))
		print "-------_"
		reply = data
		

		self.response.out.write(data)


	def get(self):

		#return
		XX = "XssssX"
		way = Waypoint.get_by_key_name(XX)
		if way:
			way.lat = -0041.708055999999999
			way.lng = 087.289982999999999
			way.put()
		else:
			way = Waypoint(key_name=XX, ident=XX, lat=2.3, lng=6.8)
			way.put()
		way.index()
	
		self.response.out.write("OK get")

		return
		template_vars = {}
		#template_vars['app'] = {'title': 'FG-Data-Developement version', 'version': '0.1-Alpha'}
		template_vars['settings'] = settings
		template_vars['files'] = ['foo']

		path = settings.templates_path + '/foo.html'

		self.response.out.write(template.render(path, template_vars))