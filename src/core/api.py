from os import environ
from tweepy import *

class Api:

	__CONSUMER_KEY = str(environ['CONSUMER_KEY'])
	__CONSUMER_SECRET = str(environ['CONSUMER_SECRET'])

	__BEARER_TOKEN = str(environ['BEARER_TOKEN'])

	__ACCESS_TOKEN = str(environ['ACCESS_TOKEN'])
	__ACCESS_TOKEN_SECRET = str(environ['ACCESS_TOKEN_SECRET'])

	_client: Client

	def __init__(self) -> None:
		self.connect()

	def connect(self) -> bool:
		try:
			self._client = Client(self.__BEARER_TOKEN)
			tweets = self._client.get_tweets([1614635180324524032])
			print("[i] - api connection is ok !")
			return True

		except Exception as e:
			print("[i] - api connection failed bruh :(")
			return False
