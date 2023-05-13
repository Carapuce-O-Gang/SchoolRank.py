from os import environ
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

from core.models import *

class Datasource:

	__client: Client = None
	__transport: RequestsHTTPTransport = None

	def __init__(self) -> None:
		self.connect()

		print(self.__client)

	def connect(self) -> bool:
		self.__transport = RequestsHTTPTransport(url = environ['DATABASE_URL'])
		self.__client = Client(
			transport = self.__transport,
			fetch_schema_from_transport = True
		)

		return True
