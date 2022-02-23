# Python BeautifulSoup saving to CSV


from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import csv

r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
soup=BeautifulSoup(r.content,'html.parser')
titles=soup.find_all('div',attrs={'class','head'})
titles_list=[]
count=1
for title in titles:
	d={}
	d['Title Number']=f'Title{count}'
	d['Title Name']=title.text
	count=count+1
	titles_list.append(d)
filename='titles.csv'
with open(filename,'w',newline='')as f:
	w=csv.DictWriter(f,['Title Number','Title Name'])
	w.writeheader()
	w.writerows(titles_list)