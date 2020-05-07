# import libraries
from bs4 import BeautifulSoup
import urllib.request
import requests
import csv
import xlsxwriter

# Specify the url to scrape
urlpage = 'http://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/'

# Get page contelt
page = requests.get(urlpage)

# Parse the html using beautifulsoup
soup = BeautifulSoup(page.content, 'html.parser')

# Find results within table
table = soup.find('table', attrs={'class': 'tableSorter2'})
results = table.find_all('tr')
print('Number of results: ', len(results))

# create and write headers to a list
rows = []
rows.append(['Rank', 'Company Name', 'Webpage', 'Description', 'Location', 'Year end', 'Annual sales rise over 3 years', 'Sales £000s', 'Staff', 'Comments'])
print(rows)

# Loop over results
for result in results:

	data = result.find_all('td')
	# check that colums have data
	if len(data) == 0:
		continue

	# write columns to variables
	rank = data[0].getText()
	location = data[2].getText()
	yearend = data[3].getText()
	salesrise = data[4].getText()

	sales = data[5].getText()
	sales = sales.strip('*').strip('†').replace(',','')

	staff = data[6].getText()
	comments = data[7].getText() 

	# extract compagny name  and description from data[1]
	company = data[1].getText()
	companyname = data[1].find('span', attrs={'class':'company-name'}).getText()	
	description = company.replace(companyname, '')

	# extract company website
	link = data[1].find('a').get('href')
	page = requests.get(link)
	soup2 = BeautifulSoup(page.content, 'html.parser')
	try:
		table_row = soup2.find('table').find_all('td')[-1]
		webpage = table_row.find('a').get('href')
	except:
		webpage = None
	# print(webpage)

	# write each result t rowns
	rows.append([rank, companyname, webpage, description, location, yearend, salesrise, sales, staff, comments])

print(rows)

# Create csv and write rows to csv file
with open('fasttack2019.csv', 'w', newline='') as file:
	csv_file = csv.writer(file)
	csv_file.writerows(rows)


# Create excel and write rows to xlsx file
with xlsxwriter.Workbook('fasttrack2019.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
    for row_num, data in enumerate(rows):
        worksheet.write_row(row_num, 0, data)
