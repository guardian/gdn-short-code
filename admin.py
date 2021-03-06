import webapp2
import jinja2
import os
import json
import logging
from urllib import quote, urlencode
from google.appengine.api import urlfetch

import configuration

from models import Configuration

import repositories

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")))

class AdminPage(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('admin/index.html')
		
		template_values = {}

		self.response.out.write(template.render(template_values))

class ConfigurationPage(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('admin/configuration.html')
		
		template_values = {}

		template_values['configuration'] = Configuration.query()

		self.response.out.write(template.render(template_values))

	def post(self):
		key = self.request.POST['key']
		value = self.request.POST['value']
		#map(lambda x: logging.info(x), [key, value])

		configuration.create(key, value)

		return webapp2.redirect('/admin/configuration')

class ShortcodesPage(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('admin/short-codes.html')
		
		template_values = {
			"campaigns": ["Facebook", "Twitter"],
			"short_codes": repositories.short_codes.all(),
		}

		self.response.out.write(template.render(template_values))

	def post(self):

		data = self.request.POST

		name = data.get("name")
		code = data.get("campaign_code")
		campaign = data.get("campaign")

		repositories.short_codes.create(name, code, campaign)

		return webapp2.redirect('/admin/short-codes')

class ShortcodeDeletionRequest(webapp2.RequestHandler):
	def post(self):

		key = self.request.POST['key']

		logging.info(key)

		repositories.short_codes.delete(key)

		return webapp2.redirect('/admin/short-codes')

app = webapp2.WSGIApplication([
	('/admin/configuration', ConfigurationPage),
	('/admin/short-codes', ShortcodesPage),
	('/admin/short-codes/delete-form', ShortcodeDeletionRequest),
	('/admin', AdminPage),],
                              debug=True)