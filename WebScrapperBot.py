from bs4 import BeautifulSoup
import requests
import csv

try:
    source = requests.get('https://www.cbinsights.com/research/well-funded-startups-us-map/')g
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
    name = soup.find('tbody').find_all('tr')

    print(source.status_code)

    with open('startuporg.csv', 'w', newline='') as starter:
        fieldnames = ['Location', 'Name', 'Total Equity']
        writer = csv.DictWriter(starter, fieldnames=fieldnames)

        writer.writeheader()

        for startup in name:
            company_loc = startup.find_all('td')[0].text
            company_name = startup.find_all('td')[1].text
            equity = startup.find_all('td')[2].text

            writer.writerow({'Location': company_loc, 'Name': company_name, 'Total Equity': equity})
            print(company_loc, company_name, equity)
except Exception as e:
    print(e)