import csv
import StringIO

import data

columns = {
	'campaign': 3,
	'section': 5,
}

def output_data(row):
	return {'name': row[10], 'code': row[0]}

def read_codes():
	return filter(lambda row: len(row) > 0,
		csv.reader(StringIO.StringIO(data.codes_csv), csv.excel))

def valid_short_code(section, short_code_row):

	campaign_section = short_code_row[5]
	campaign_code = short_code_row[3]
	valid_campaigns = {'Twitter', 'Facebook', 'Instagram', 'Tumblr'}
	if campaign_code in valid_campaigns:
		if not section:
			return True

		if not campaign_section:
			return True

		if section and section == campaign_section:
			return True

	return False

def general_short_code(short_code_row):

	campaign_section = short_code_row[columns['section']]
	campaign_code = short_code_row[columns['campaign']]

	valid_campaigns = {'Twitter', 'Facebook', 'Instagram', 'Tumblr'}

	if campaign_code in valid_campaigns and not campaign_section:
		return True

	return False

def section_specific_codes(section, short_code_data):
	if not section:
		return []
	return [output_data(row) for row in short_code_data if row[columns['section']] == section]

def codes(section=None):

	all_codes = read_codes()

	general_codes = [output_data(row) for row in all_codes if general_short_code(row)]

	return section_specific_codes(section, all_codes) + general_codes
