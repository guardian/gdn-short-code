
from google.appengine.ext import ndb

class ShortCode(ndb.Model):
	name = ndb.StringProperty(required=True)
	code = ndb.StringProperty(required=True)
	campaign = ndb.StringProperty(required=True)

def create(name, code, campaign):
	short_code = ShortCode(name=name, code=code, campaign=campaign)
	short_code.put()

	return short_code

def all():

	return [sc for sc in ShortCode.query()]