import requests
from bs4 import BeautifulSoup
response=requests.get("https://www.google.com")
#print(response.text)
soup=BeautifulSoup(response.text, 'html.parser')
title=soup.find('title').text
print(f"ページのタイトル{title}")
