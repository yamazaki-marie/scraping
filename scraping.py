import requests
import re
from bs4 import BeautifulSoup
def search_word(url,word):
    response=requests.get(url)
    #print(response.text)
    soup=BeautifulSoup(response.text, 'html.parser')
    elems = soup.find_all(string=re.compile(word))
    return elems
results=search_word("https://yahoo.co.jp","一休")
for result in results:
    print(results)