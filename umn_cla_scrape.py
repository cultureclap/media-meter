import requests
from pprint import pprint as ppr

from lxml import html


def getSite(link):
	page = requests.get(link)
	code = html.fromstring(page.text)
	return code

def getLinks(code):
	links = code.xpath('.//*/a')
	return links

def getEmail(links):
	emails = []
	links1 = links.xpath('.//@href')
	links2 = links.xpath('.//*/@href')
	total_links = links1 + links2

	for link in total_links:
		if link.startswith('mailto:'):
			emails.append(link.replace('mailto:', ''))
	return emails


page = requests.get("https://cla.umn.edu/academics-experience/departments-centers")

# print(dir(page))

pageInfo = html.fromstring(page.text)

# ppr(pageInfo)

deptsTable = pageInfo.xpath('.//*/div[@id="cla-landing-two-column-stacked-main"]/div/div/div/div/a')

# ppr(deptsTable)

dpts = []

for dt in deptsTable:
	link = dt.xpath('.//@href')[0]
	name = dt.xpath('.//div[@class="field-display-name"]/text()')
	# print(name, link)
	if link.startswith("https://"):
		dept = {}
		dept['title'] = name[0].replace('\n', '').strip()
		dept['link'] = link
		# print(dept)
		dpts.append(dept)

# ppr(dpts)

for dpt in dpts:
	code = getSite(dpt['link'])
	links = code.xpath('.//*/a/@href')
	for link in links:
		# print(link)
		if link.startswith('http://twitter'):
			print(link)
	# ppr(links)