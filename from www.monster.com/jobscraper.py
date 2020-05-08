
# import librairies
from bs4 import BeautifulSoup
import requests


# Open url
url = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(url)

# Parse the html using beautifulsoup
soup = BeautifulSoup(page.content, 'html.parser')

# find results using html id
results = soup.find(id='SearchResults')

# find job elements by class name
job_elements = results.find_all('section', attrs={'class': 'card-content'})
# print(job_elements[0].prettify())


# Extracting job title, company name, and job location
rows = []
rows.append(["Job Title", "Company Name", "Job Location"])
for job_element in job_elements:
	try:
		job_title = job_element.find('h2', attrs={'class': 'title'}).text
		company_name = job_element.find('div', attrs={'class': 'company'}).text
		location = job_element.find('div', attrs={'class': 'location'}).text	
	except AttributeError:
		continue

	rows.append([job_title.strip(), company_name.strip(), location.strip()])
	print(job_title.strip())
	print(company_name.strip())
	print(location.strip())
	print()

print(rows)

# Filter only Job Analyst
analyst_jobs = results.find_all('h2', string=lambda text: 'analyst' in text.lower())
print(len(analyst_jobs))

