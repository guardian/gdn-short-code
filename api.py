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

		payload = {
			'show-fields': 'shortUrl,linkText',
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

		code_reader = csv.reader(StringIO.StringIO(data.codes_csv), csv.excel)

		def valid_short_code(short_code_row):
			if not len(row) > 0:
				return False

			campaign_section = short_code_row[5]
			campaign_code = short_code_row[3]
			valid_campaigns = {'Twitter', 'Facebook', 'Instagram', 'Tumblr'}
			if campaign_code in valid_campaigns:
				if not section:
					return True

				if not campaign_section:
					return True

				if section and section == campaign_section:
					return True

			return False


		codes = [{'name': row[10], 'code': row[0]} for row in code_reader if valid_short_code(row)]

		self.response.write(json.dumps(codes))

app = webapp2.WSGIApplication([
	webapp2.Route(r'/api/short-url', handler=ShortUrlLookup),
	webapp2.Route(r'/api/short-codes', handler=ShortCodes),
	webapp2.Route(r'/api/short-codes/section/<section>', handler=ShortCodes),],
                              debug=True)