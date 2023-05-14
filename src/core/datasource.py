import json
from os import environ
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

from core.models import *

class Datasource:

	__client: Client = None
	__transport: RequestsHTTPTransport = None

	def __init__(self) -> None:
		self._connect()
		self._check_connection()

	def _connect(self) -> None:
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

	def _check_connection(self) -> bool:
		query = gql("""query {
			school(where: { id: "" }) {
				id
				name
			}
		}""")

		try:
			response = self.__client.execute(query)
			print(f"[OK]: Connexion with hygraph is etablished")
			return True

		except Exception as err:
			print(f"[ERR]: {err}")
			return False
	
	def get_schools(self) -> dict:
		query = gql("""query {
			schools {
				id
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

		return self.__client.execute(query)

	def get_school(self, id: str) -> dict:
		query = gql("""query {
			school(where: { id: "%s" }) {
				id
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
		}""" % id)

		print(self.__client.execute(query))
