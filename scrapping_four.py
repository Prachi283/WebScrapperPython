# Extracting Text from the tags

from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
soup=BeautifulSoup(r.content,'html.parser')
# print(soup.prettify())

# 1.  Removing the tags from the content of the page

s=soup.find('div',class_="entry-content")
# print(s)
lines=s.find_all('p')
# for line in lines:
# 	print(line.text)
s=soup.find('div',class_="header-main__slider")
# print(s)
d=s.find_all('ul')
# print(d)
d1=soup.find('ul',id="hslider")
# print(d1)
l1=d1.find_all('li')
# print(l1)
li_data=[]
for l in l1:
	li_data.append(l.text)
# print(li_data)
for i in li_data:
	print(i,'\n')