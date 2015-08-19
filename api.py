import webapp2
import jinja2
import os
import json
import logging
from urllib import quote, urlencode
from google.appengine.api import urlfetch

class ShortUrlLookup(webapp2.RequestHandler):
	def get(self):
		shortUrl = 'http://shorturl'

		self.response.write(json.dumps({'shortUrl': shortUrl}))

class ShortCodes(webapp2.RequestHandler):
	def get(self):
		payload = [{'name': 'Twitter', 'code': 'twt'},] 
		self.response.write(json.dumps(payload))

app = webapp2.WSGIApplication([
	webapp2.Route(r'/api/short-url', handler=ShortUrlLookup),
	webapp2.Route(r'/api/short-codes', handler=ShortCodes),],
                              debug=True)