# Extracting Links
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
soup=BeautifulSoup(r.content,'html.parser')

s=soup.find('div',class_="Basics")
# print(s)
list1=s.find_all('a')
# print(list1)
# Printing all Links **************
for link in list1:
	print(link)

# Printing text inside the links **********
for link in list1:
	print(link.text)
	
