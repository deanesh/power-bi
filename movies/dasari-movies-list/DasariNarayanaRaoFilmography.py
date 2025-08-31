import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url = "https://en.wikipedia.org/wiki/Dasari_Narayana_Rao"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

films = []

# Find the h2 tag whose text contains "Filmography"
filmography_header = None
for h2 in soup.find_all('h2'):
    # h2.text includes the "edit" link text, so check for 'Filmography' in text
    if 'Filmography' in h2.text:
        filmography_header = h2
        break

if filmography_header:
    sibling = filmography_header.find_next_sibling()
    # Loop through siblings until the next h2 (next section)
    while sibling and sibling.name != 'h2':
        if sibling.name == 'p':
            links = sibling.find_all('a')
            for link in links:
                movie_name = link.get_text(strip=True)
                next_sibling_text = link.next_sibling
                year = None
                if next_sibling_text:
                    match = re.search(r'\((\d{4})\)', next_sibling_text)
                    if match:
                        year = match.group(1)
                films.append({'Movie_Name': movie_name, 'Release_Year': year})
        sibling = sibling.find_next_sibling()
else:
    print("No Filmography header found.")

df = pd.DataFrame(films)
if 'Movie_Name' in df.columns:
    df = df.dropna(subset=['Movie_Name']).drop_duplicates().reset_index(drop=True)
else:
    print("No Movie_Name column found.")
    df = pd.DataFrame()

print(df.head(20))
