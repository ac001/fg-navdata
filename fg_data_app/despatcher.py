# -*- coding: utf-8 -*-

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from pages.IndexPage import IndexPage
from pages.WaypointsPage import WaypointsPage
from pages.FooPage import FooPage

application = webapp.WSGIApplication([	('/', IndexPage),
										('/waypoints', WaypointsPage),
										('/foo', FooPage),
									 ], debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()