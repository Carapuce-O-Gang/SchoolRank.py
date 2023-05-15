from os import environ
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from time import sleep

class Datasource:

	__client: Client = None
	__transport: RequestsHTTPTransport = None

	def __init__(self) -> None:
		self._connect()
		self._check()

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

	def _check(self) -> bool:
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

		return self.__client.execute(query)['schools']

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

		return self.__client.execute(query)['school']
	
	def create_school(self, create_school_record) -> str:
		school = """
            createSchool(data: {
                name: "%s"
                sector: "%s"
                type: "%s"
                department: "%s"
                academy: "%s"
                city: "%s"
                uai: "%s"
                insee: %d
                promotion: "%s"
                zip: "%s"
				latitude: %f
				longitude: %f
        """ % (
            create_school_record.get('fields', {}).get('nom_de_l_etablissment'),
            create_school_record.get('fields', {}).get('secteur'),
            create_school_record.get('fields', {}).get('type_de_lycee'),
            create_school_record.get('fields', {}).get('departement'),
            create_school_record.get('fields', {}).get('academie'),
            create_school_record.get('fields', {}).get('nom_de_la_commune'),
            create_school_record.get('fields', {}).get('uai'),
            int(create_school_record.get('fields', {}).get('code_insee_de_la_commune', 0)),
            create_school_record.get('fields', {}).get('rentree_scolaire'),
            create_school_record.get('fields', {}).get('code_du_departement'),
	    	0,
		    0
        )

		if 'ips_ensemble_gt_pro' in create_school_record['fields']:
			school += 'ips: %d\n' % (int(create_school_record['fields']['ips_ensemble_gt_pro']))

		if 'ips_voie_gt' in create_school_record['fields']:
			school += 'ipsGt: %d\n' % (int(create_school_record['fields']['ips_voie_gt']))
		
		if 'ips_voie_pro' in create_school_record['fields']:
			school += 'ipsPro: %d\n' % (int(create_school_record['fields']['ips_voie_pro']))

		school += """})  {
                name
                sector
                type
                department
                academy
                city
                uai
                insee
                promotion
                zip
		"""

		if 'ips_ensemble_gt_pro' in create_school_record['fields']:
			school += 'ips\n'

		if 'ips_voie_gt' in create_school_record['fields']:
			school += 'ipsGt\n'

		if 'ips_voie_pro' in create_school_record['fields']:
			school += 'ipsPro\n'

		school += '}\n'

		return school

	def create_schools(self, records: list) -> None:

		for i in range(len(records)):
			print(records[i]['fields']['nom_de_l_etablissment'])
			school = self.create_school(records[i])

			mutation = """
				mutation {
					%s
				}	
			""" % (school)

			query = gql(mutation)

			sleep(0.25)

			self.__client.execute(query)
