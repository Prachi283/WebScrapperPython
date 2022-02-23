# Finding Elements 
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
soup=BeautifulSoup(r.content,'html.parser')
# print(soup.prettify())

# 1. Finding Elements by class

s=soup.find('div',class_='entry-content')
content=s.find_all('p')
# print(content)

# 2. Finding Elements by ID 

s_id=soup.find('div',id="main")
# print(s_id)
for s1 in s_id:
	c=soup.find('div',class_="leftbar-dropdown")
	# print(c)

for anchr in s_id:
	c1=soup.find_all('a')
	# print(c1)

s = soup.find('div', id= 'main')
 
# Getting the leftbar
leftbar = s.find('ul', class_='leftBarList')
 
# All the li under the above ul
content = leftbar.find_all('li')
 
print(content)

