#!/usr/bin/python3
import os
import requests
from bs4 import BeautifulSoup


base_url_input = input('================================================\nCopas Url ^_^\n================================================\nContoh URL:http://books.toscrape.com\n================================================\nDISINI :  ')


page_request = requests.get(base_url_input)
page_obj = page_request.content

soup = BeautifulSoup(page_obj, "html.parser")


images = soup.find_all("img")

for image in images:
    os.system("wget -P ~/Pictures/ScrappingImage " + base_url_input + '/' + image.attrs["src"])