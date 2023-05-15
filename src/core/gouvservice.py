import requests
import json
from gql import gql
from os import environ
from core.datasource import Datasource
from core.geolocation import Geolocation

class GouvService:

	def get_data(self) -> list:
		raw_data_set = requests.get(environ['DATA_SET_URL']).text
		data_set = json.loads(raw_data_set)

		return data_set['records']
	
	def get_school(self, record) -> str:
		geo = Geolocation()
		geoloc = geo.getGeoloc(record.get('fields', {}).get('code_insee_de_la_commune', 0))

		school = """
			createSchool(data: {
				name: "%s"
				sector: "%s"
				type: "%s"
				department: "%s"
				academy: "%s"
				city: "%s"
				longitude: %f
				latitude: %f
				uai: "%s"
				insee: %d
				promotion: "%s"
				zip: "%s"
		""" % (
			record.get('fields', {}).get('nom_de_l_etablissment'),
			record.get('fields', {}).get('secteur'),
			record.get('fields', {}).get('type_de_lycee'),
			record.get('fields', {}).get('departement'),
			record.get('fields', {}).get('academie'),
			record.get('fields', {}).get('nom_de_la_commune'),
			float(geoloc['longitude']),
			float(geoloc['latitude']),
			record.get('fields', {}).get('uai'),
			int(record.get('fields', {}).get('code_insee_de_la_commune', 0)),
			record.get('fields', {}).get('rentree_scolaire'),
			record.get('fields', {}).get('code_du_departement')
		)

		if 'ips_ensemble_gt_pro' in record['fields']:
			school += 'ips: %f\n' % (float(record['fields']['ips_ensemble_gt_pro']))

		if 'ips_voie_gt' in record['fields']:
			school += 'ipsGt: %f\n' % (float(record['fields']['ips_voie_gt']))

		if 'ips_voie_pro' in record['fields']:
			school += 'ipsPro: %f\n' % (float(record['fields']['ips_voie_pro']))

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
				zip"""

		if 'ips_ensemble_gt_pro' in record['fields']:
			school += 'ips\n'

		if 'ips_voie_gt' in record['fields']:
			school += 'ipsGt\n'

		if 'ips_voie_pro' in record['fields']:
			school += 'ipsPro\n'

		school += '}\n'

		return school

	def populate(self) -> None:
		records = self.get_data()
		gql_client = Datasource().get_client()

		schools = []

		for i in range(len(records)):
			schools.append(self.get_school(records[i]))

		mutation = """
			mutation {
				%s
			}
		""" % ("\n".join(schools))

		print(mutation)

		query = gql(mutation)
		result = gql_client.execute(query)

		print(result)


