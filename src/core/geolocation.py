import json

class Geolocation:

	__cities: dict

	def __init__(self) -> None:
		self.__cities = json.load(open('./core/cities.json'))['cities']

	def getGeoloc(self, insee: str) -> dict:
		for citie in self.__cities:
			if(insee == citie['insee_code']):
				return({ "latitude": citie['latitude'], "longitude": citie['longitude'] })
		
		return({ "latitude": 0.00, "longitude": 0.00 })