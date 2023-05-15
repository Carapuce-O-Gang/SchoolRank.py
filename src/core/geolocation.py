import json

class Geolocation:

	__cities: dict

	def __init__(self) -> None:
		self.__cities = json.load(open('./core/cities.json'))['cities']
		self.getGeoloc('77')

	def getGeoloc(self, insee: str) -> dict:
		for citie in self.__cities:
			print(citie['insee_code'])