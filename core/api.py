from os import environ
from tweepy import *

class Api:

	CONSUMER_KEY = str(environ['CONSUMER_KEY'])
	CONSUMER_SECRET = str(environ['CONSUMER_SECRET'])

	ACCESS_TOKEN = str(environ['ACCESS_TOKEN'])
	ACCESS_TOKEN_SECRET = str(environ['ACCESS_TOKEN_SECRET'])

	def __init__(self):
		self.auth = OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
		self.auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)

		self.connect()
	
	def connect(self):
		self.remote = API(self.auth)
		self.remote.update_status("Hello tweepy")
