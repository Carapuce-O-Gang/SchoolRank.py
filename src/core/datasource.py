from os import environ
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

from core.models import *

class Datasource:

	__client = None
	__transport = None

	def __init__(self) -> None:
		self.connect()

		print(self.__client)

	def connect(self) -> bool:
		self.__transport = RequestsHTTPTransport(
			url=environ['DATABASE_URL'],
			headers={
				'Authorization': environ['DATABASE_TOKEN']
			}
		)
		self.__client = Client(
			transport=self.__transport,
			fetch_schema_from_transport=True
		)

		return True
	
	def get_client(self) -> dict:
		return self.__client
