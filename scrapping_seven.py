# Scraping multiple Pages

from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
soup=BeautifulSoup(r.content,'html.parser')

# 1. Looping through the page numbers **********
titles = soup.find_all('div',attrs = {'class','head'})
# print(titles[0].text)
for i in range(7):
	print(titles[i].text)