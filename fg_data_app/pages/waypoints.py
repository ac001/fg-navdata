# -*- coding: utf-8 -*-

import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template


class WaypointsPage(webapp.RequestHandler):
  def get(self):

	template_vars = {}
	template_vars['app'] = {'title': 'FG-Data-Developement version', 'version': '0.1-Alpha'}
	template_vars['files'] = ['waypoints']
	template_vars['file_types'] = ['json', 'yaml']
	path = os.path.join(os.path.dirname(__file__), 'templates/index.html')

	self.response.out.write(template.render(path, template_vars))

application = webapp.WSGIApplication(
                                     [('/waypoints', WaypointsPage),],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()