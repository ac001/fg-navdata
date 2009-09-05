# -*- coding: utf-8 -*-

import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

import settings

class IndexPage(webapp.RequestHandler):
  def get(self):

	template_vars = {}
	#template_vars['app'] = {'title': 'FG-Data-Developement version', 'version': '0.1-Alpha'}
	template_vars['settings'] = settings
	template_vars['files'] = ['waypoints']
	
	path = os.path.join(os.path.dirname(__file__), 'templates/index.html')

	self.response.out.write(template.render(path, template_vars))

