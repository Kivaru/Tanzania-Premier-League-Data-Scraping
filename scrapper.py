# import pandas as pd
# from bs4 import BeautifulSoup
# import time
# import requests
#
# url = "https://ligikuu.co.tz/statistics/"
#
# response = requests.get(url)
#
# soup = BeautifulSoup(response.content, "html.parser")
#
# goals_stats = []
#
# table = soup.find("table", class_="sp-player-list")
#
# headers = []
# for th in table.find_all("th"):
#     headers.append(th.text.strip())
#
# for row in soup.select('tbody tr'):
#     player = row.find('td', class_='data-name has-photo').find('a').get_text()
#     club = row.find('td', class_='data-team').find('a').get_text()
#     position = row.find('td', class_='data-position').get_text()
#     goals = row.find('td', class_='data-goals').get_text()
#
#     goals_stats.append([player, club, position, goals])
#
# df = pd.DataFrame(goals_stats, columns=['Player', 'Club', 'Position', 'Goals'])
#
# time.sleep(1)
#
# df.to_csv('goals-stats.csv', index=False)

import requests
from bs4 import BeautifulSoup

url = "https://ligikuu.co.tz/statistics"
response = requests.get(url)


soup = BeautifulSoup(response.content, "html.parser")
print(soup)

table = soup.find("table", class_="sp-player-list")
# headers = []
# for th in table.find_all("th"):
#     headers.append(th.text.strip())

rows = []
for row in table.find_all("tr"):
    cells = []
    for td in row.find_all("td"):
        cells.append(td.text.strip())
    if cells:
        rows.append(cells)

# Process the extracted data
# print(headers)
# for row in rows:
#     print(row)
print(rows)