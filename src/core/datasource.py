import json
from os import environ
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

from core.models import *

class Datasource:

	__client: Client = None
	__transport: RequestsHTTPTransport = None

	def __init__(self) -> None:
		self.connect()
		self.check_connection()

	def check_connection(self) -> bool:
		query = query = gql("""query {
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

		try:
			response = self.__client.execute(query)
			print(f"[OK]: Connexion with hygraph is etablished")
			return True

		except Exception as err:
			print(f"[ERR]: {err}")
			return False

	def connect(self) -> None:
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
