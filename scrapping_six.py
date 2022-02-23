 # Extracting Image Information

from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
soup=BeautifulSoup(r.content,'html.parser')

images_list=[]

images=soup.select('img')
# print(images)

for image in images:
	alt=image.get('alt')
	src=image.get('src')
	images_list.append({'alt':alt,'src':src})
# print(images_list)
for im in images_list:
	print(im)




# images = soup.select('img')
# for image in images:
# 	src = image.get('src')
# 	alt = image.get('alt')
# 	images_list.append({"src": src, "alt": alt})
	
# for image in images_list:
# 	print(image)
