from os import environ
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

from core.models import *

class Datasource:

	__client: Client = None
	__transport: RequestsHTTPTransport = None

	def __init__(self) -> None:
		self.connect()

		query = gql("""query {
			schools {
				name
				type
				sector
				zip
				department
				academy
				city
				uai
				insee
				promotion
				ips
				ipsGt
				ipsPro
			}
		}""")

		print(self.__client.execute(query))

	def connect(self) -> bool:
		self.__transport = RequestsHTTPTransport(
			url = environ['DATABASE_URL'],
			headers = {
				"Authorization": f"Bearer {environ['DATABASE_TOKEN']}"
			}
		)

		self.__client = Client(
			transport = self.__transport,
			fetch_schema_from_transport = True
		)

		return True
