import logging
import csv
import StringIO

import data

columns = {
	'campaign': 3,
	'section': 5,
}

premier_campaigns = {'Twitter', 'Facebook', 'Instagram', 'Tumblr'}

def output_data(row):
	return {'name': row[10], 'code': row[0]}

def read_codes():
	return filter(lambda row: len(row) > 0,
		csv.reader(StringIO.StringIO(data.codes_csv), csv.excel))

def valid_short_code(short_code_row, section=None):

	campaign_section = short_code_row[5]
	campaign_code = short_code_row[3]

	if campaign_code in premier_campaigns:
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

	if campaign_code in premier_campaigns and not campaign_section:
		return True

	return False

def check_section(section, short_code_row):
	row_section = short_code_row[columns['section']]

	if 'sport' in section and row_section in ['sport', 'football']:
			return True

	if row_section in [section]:
		return True

	return False


def section_specific_codes(section, short_code_data):
	if not section:
		return []
	return [output_data(row) for row in short_code_data if check_section(section, row) and row[columns['campaign']] in premier_campaigns]

def codes(section=None):

	all_codes = read_codes()

	if not section:
		return [output_data(row) for row in all_codes if valid_short_code(row)]

	general_codes = [output_data(row) for row in all_codes if general_short_code(row)]

	return section_specific_codes(section, all_codes) + general_codes
