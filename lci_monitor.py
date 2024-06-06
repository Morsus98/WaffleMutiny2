import requests
from bs4 import BeautifulSoup

url = "https://www.mtgstocks.com/sets/1182-the-lost-caverns-of-ixalan"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
table = soup.find("table", {"class": "cardstable"})

if table:
    headers = [th.text.strip() for th in table.find("tr").find_all("th")]
    rows = []
    for row in table.find_all("tr")[1:]:
        rows.append([td.text.strip() for td in row.find_all("td")])

    print("Headers:", headers)
    print("Data:")
    for row in rows:
        print(row)
else:
    print("Table not found on the webpage.")