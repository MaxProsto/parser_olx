from bs4 import BeautifulSoup
import requests

product = input()

url = "https://www.olx.uz/list/q-/" + product
request = requests.get( url )
bs = BeautifulSoup( request.text, "html.parser" )

all_links = bs.find_all("a", class_="linkWithHash")

for link in all_links:
  print("https://www.olx.uz" + link[ "href" ] )