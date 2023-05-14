class School:

	__name: str
	__type: str
	__sector: str
	__zip: str
	__department: str
	__academy: str
	__city: str
	__uai: str
	__insee: int
	__promotion: str
	__ips: float
	__ipsGt: float
	__ipsPro: float

	def __init__(self, name: str, type: str, sector: str, zip: str, department: str, academy: str, city: str, uai: str, insee: int, promotion: str, ips: float, ipsGt: float, ipsPro: float) -> None:
		self.__name = name
		self.__type = type
		self.__sector = sector
		self.__zip = zip
		self.__department = department
		self.__academy = academy
		self.__city = city
		self.__uai = uai
		self.__insee = insee
		self.__promotion = promotion
		self.__ips = ips
		self.__ipsGt = ipsGt
		self.__ipsPro = ipsPro

		pass
