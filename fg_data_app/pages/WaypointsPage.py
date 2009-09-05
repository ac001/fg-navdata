# -*- coding: utf-8 -*-

import os
import yaml

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

import settings



class WaypointsPage(webapp.RequestHandler):
	def get(self):

		#pth = os.path.join(os.path.dirname(__file__), '../yaml')
		#files = {} #os.listdir(settings.root_path + '/js')
		info_file_name = settings.root_path + '/info/waypoints.yaml'
		info = yaml.load(open(info_file_name, 'r'))
		info_list = []
		for i in info:
			s = "<h3>%s</h3>" % i
			s += "<p>%s</p>" % info[i]['description']
			s += "<pre>%s</pre>" % info[i]['snippet']
			info_list.append( s )

		template_vars = {}
		template_vars['settings'] = settings
		template_vars['info_list'] = info_list
		path = os.path.join(os.path.dirname(__file__), 'templates/waypoints.html')
		
		self.response.out.write(template.render(path, template_vars))

