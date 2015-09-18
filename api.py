import webapp2
import jinja2
import os
import json
import logging
from urllib import quote, urlencode

from google.appengine.api import urlfetch

import content_api
import short_codes
import headers

class ShortUrlLookup(webapp2.RequestHandler):
	def get(self):
		path = self.request.get('path')

		payload = {
			'show-fields': 'shortUrl,linkText,trailText',
		}

		content_data = content_api.read(path, payload)

		if not content_data:
			webapp2.abort(404, 'Url not found in the content API')
			return

		content_json = json.loads(content_data)

		content = content_json.get('response', {}).get('content', {})

		self.response.write(json.dumps(content))

class ShortCodes(webapp2.RequestHandler):
	def get(self, section=None):
		headers.json(self.response)

		self.response.write(json.dumps(short_codes.codes(section)))

app = webapp2.WSGIApplication([
	webapp2.Route(r'/api/short-url', handler=ShortUrlLookup),
	webapp2.Route(r'/api/short-codes', handler=ShortCodes),
	webapp2.Route(r'/api/short-codes/section/<section>', handler=ShortCodes),],
                              debug=True)