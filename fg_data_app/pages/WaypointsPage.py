# -*- coding: utf-8 -*-

import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

import settings

class WaypointsPage(webapp.RequestHandler):
	def get(self):

		template_vars = {}
		template_vars['settings'] = settings
		path = os.path.join(os.path.dirname(__file__), 'templates/waypoints.html')

		

		self.response.out.write(template.render(path, template_vars))

