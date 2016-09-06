import logging
import csv
import StringIO

import data_ga
import repositories

columns = {
	'campaign': 0,
	'section': 6,
}

premier_campaigns = {'Twitter', 'Facebook', 'Instagram', 'Tumblr', 'Pinterest'}

parent_sections = {
	'culture': ['film', 'music', 'tv-and-radio', 'stage', 'books', 'artanddesign'],
	'sport': ['football'],
}

def output_data(row):
	return {'name': row[2],
			'code': '',
			'campaign': row[2],
			'utm_campaign' : row[2],
			'utm_sourceutm_source' : row[0],
			'utm_medium' : row[1],
			'utm_content' : row[3],
			'utm_term' : row[4],
			'INTCMP' : row[5]
			}

def read_codes():
	data = data_ga
	return filter(lambda row: len(row) > 0,
		csv.reader(StringIO.StringIO(data.codes_csv), csv.excel))

def valid_short_code(short_code_row, section=None):

	campaign_section = short_code_row[6]
	campaign_code = short_code_row[0]

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

	for parent_section, sub_sections in parent_sections.items():
		for sub_section in sub_sections:
			if sub_section in section and row_section in [sub_section, parent_section]:
				logging.info('1')
				return True

	if row_section in [section]:
		return True
	return False


def section_specific_codes(section, short_code_data):
	if not section:
		return []
	return [output_data(row) for row in short_code_data if check_section(section, row) and row[columns['campaign']] in premier_campaigns]

def codes(section=None):

	data_codes = [{"name": sc.name, "code": sc.code} for sc in repositories.short_codes.all()]

	all_codes = read_codes()

	if not section:
		return [output_data(row) for row in all_codes if valid_short_code(row)] + data_codes

	general_codes = [output_data(row) for row in all_codes if general_short_code(row)]

	return section_specific_codes(section, all_codes) + general_codes + data_codes
