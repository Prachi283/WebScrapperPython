from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# 1. Python requests making GET request  *****************************
# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.content)

# 2.Python requests Response Object *****************************
print(r.status_code)

# 3. Python BeautifulSoup Parsing HTML  ***************************

soup=BeautifulSoup(r.content,'html.parser')
print(soup.prettify())

# 4. Getting Tags *******************************
# Getting the title tag
print(soup.title)

# Getting the name of the tag
print(soup.title.name)
 
# Getting the name of parent tag
print(soup.title.parent.name)
 
print(soup.title.text)    # Printing the text inside the title tag