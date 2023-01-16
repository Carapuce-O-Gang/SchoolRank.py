from gql import *
from core.models import *

class Datasource:
	def __init__(self) -> None:
		self.connect()
	
	def connect(self) -> bool:
		return True