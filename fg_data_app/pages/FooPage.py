# -*- coding: utf-8 -*-

import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

import settings

import models.Airport
import models.RunwayTaxi


class FooPage(webapp.RequestHandler):
  def get(self):

	template_vars = {}
	#template_vars['app'] = {'title': 'FG-Data-Developement version', 'version': '0.1-Alpha'}
	template_vars['settings'] = settings
	template_vars['files'] = ['foo']
	
	path = settings.templates_path + '/foo.html'

	self.response.out.write(template.render(path, template_vars))