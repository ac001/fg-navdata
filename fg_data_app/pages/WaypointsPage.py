# -*- coding: utf-8 -*-

import os
import yaml

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

import settings

class WaypointsPage(webapp.RequestHandler):

	def get(self):

		info_file_name = settings.root_path + '/info/waypoints.yaml'
		info = yaml.load(open(info_file_name, 'r'))
		info_block = []
		for i in sorted(info.keys()):
			s = "<h3>%s.*</h3>" % i
			s += "<p>%s</p>" % info[i]['description']
			s += "<pre>%s</pre>" % info[i]['snippet']
			info_block.append( s )

		template_vars = {}
		template_vars['settings'] = settings
		template_vars['info'] = info
		template_vars['info_block'] = info_block
		path = os.path.join(os.path.dirname(__file__), 'templates/waypoints.html')
		
		self.response.out.write(template.render(path, template_vars))

