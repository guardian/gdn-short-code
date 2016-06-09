
from google.appengine.ext import ndb

class ShortCode(ndb.Model):
	name = ndb.StringProperty(required=True)
	code = ndb.StringProperty(required=True)
	network = ndb.StringProperty(required=True)

def create(name, code, network):
	short_code = ShortCode(name=name, code=code, network=network)
	short_code.put()

	return short_code

def all():

	return ShortCode.query()