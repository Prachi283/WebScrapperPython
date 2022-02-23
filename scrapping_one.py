import requests

from bs4 import BeautifulSoup
url="https://codewithharry.com"

# Get the HTML
r=requests.get(url)
html_content=r.content
# print(html_content)

# Parse the HTML
soup=BeautifulSoup(html_content,'html.parser')
# print(soup.prettify)

# HTML Tree Traversal

# Commonly used types of objects 
# print(type(title)) # 1.Tag
# print(title.string) # 2.NavigableString
# print(type(soup)) # 3.BeutifulSoup
# 4.Comment
# markup="<p><!--this is a Comment --></p>"
# soup2=BeautifulSoup(markup)
# print(soup2.p.string)

# Get the title of the HTML Page
title=soup.title

# Get all the paragraphs from the Pge
paras=soup.find_all('p')
# print(paras)

# Get all the Anchor tags from the Pge
anchors=soup.find_all('a')
all_links=set()
# print(anchors)
# Get all the links on the Page 
for link in anchors:
	if(link.get('href') !='/'):
		all_links.add("https://codewithharry.com" +link.get('href'))
		# print(all_links)

# Get first element in the HTML Page
# print(soup.find('p'))

# Get classes of any element in the HTML PAge
# print(soup.find('p')['class'])

# Find all the elements with class lead
# print(soup.find_all('p',class_="mt-2"))

# Get the text from the tags/soup:
# print(soup.find('p').get_text())

# print(soup.get_text())
# .contents= A tag's children are available as list
# .children= A tag's children are available as generator
searchcontent=soup.find(id='search-content')
for ele in (searchcontent.parent):
	print(ele)
