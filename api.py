import webapp2
import jinja2
import os
import json
import logging
from urllib import quote, urlencode
import csv
import StringIO

from google.appengine.api import urlfetch

import data
import content_api

class ShortUrlLookup(webapp2.RequestHandler):
	def get(self):
		path = self.request.get('path')

		content_data = content_api.read(path, {'show-fields': 'shortUrl'})

		if not content_data:
			webapp2.abort(404, 'Url not found in the content API')
			return

		content_json = json.loads(content_data)

		content = content_json.get('response', {}).get('content', {})

		self.response.write(json.dumps(content))

class ShortCodes(webapp2.RequestHandler):
	def get(self):

		code_reader = csv.reader(StringIO.StringIO(data.codes_csv), csv.excel)

		codes = [{'name': row[1], 'code': row[0]} for row in code_reader if len(row) > 0]

		self.response.write(json.dumps(codes))

app = webapp2.WSGIApplication([
	webapp2.Route(r'/api/short-url', handler=ShortUrlLookup),
	webapp2.Route(r'/api/short-codes', handler=ShortCodes),],
                              debug=True)