# use the api
# use the tool bs4
# pip installl bs4


# step 0 import all module
#pip install html5lib
#pip istall  requests

import  requests
from  bs4 import BeautifulSoup
url="https://codewithharry.com"


#  step 1 Get the Html



r=requests.get(url)
htmlContent=r.content
print(htmlContent)

# step 2 parese the Html


soup=BeautifulSoup(htmlContent,'html.parser')
print(soup.prettify)

# stp 3 Html Tree Travsersal
#commonly uses type of strinng :
#1.Tag
#2.navigable string
#3.BeautifulSoup
#4.comment
# Get the title of page
tittle=soup.title
print(type(soup))
print(type(tittle))
print(type(tittle.string))


# get all the paragraph from the page
paras=soup.find_all('p')
print(paras)
# Get all The Anchour TAgs

anchor=soup.find_all('a')
print(anchor)

# Get any class of Html content
print(soup.find('a')['class'])


# find all element with class lead
print(soup.find_all("p",class_="lead"))

# Get the text from the tags
print(soup.find_all('p').get_text())
print(soup.get_text())


# Get all the link grom all anchor tags
