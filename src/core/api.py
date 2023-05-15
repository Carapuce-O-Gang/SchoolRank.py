import requests
import json
from os import environ

class Api:

	__url: str
	__params: str

	def __init__(self) -> None:
		self._connect()
		self._check()

	def _connect(self) -> None:
		self.__url: str = environ['API_URL']
		self.__params: str = '?dataset=fr-en-ips_lycees&q=&lang=fr&rows=-1&facet=rentree_scolaire&facet=academie&facet=code_du_departement&facet=departement&facet=uai&facet=nom_de_l_etablissment&facet=code_insee_de_la_commune&facet=nom_de_la_commune&facet=secteur&facet=type_de_lycee'

	def _check(self) -> bool:
		try:
			response = requests.get(url=f"{self.__url}{self.__params}")
			print(f"[OK]: Education.gouv api is online")
			return True

		except Exception as err:
			print(f"[Err]: {err}")
			return False

	def get_records(self) -> list:
		raw_data_set = requests.get(url=f"{self.__url}{self.__params}").text
		data_set = json.loads(raw_data_set)

		return data_set['records']
