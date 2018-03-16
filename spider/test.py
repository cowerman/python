import urllib.request
import os
import re
import sys
import requests
from bs4 import BeautifulSoup

"""
#r = requests.get('http://www.pop-fashion.com/fabriczone/#gallery')
r = requests.get('http://www.pop-fashion.com/patterns/graphics/')
#print (r.text)
soup = BeautifulSoup(str(r), 'lxml')
#print (soup)
for img in soup.find_all(src="*"):
    print ("Image address: ", repr(img))

#print type(r)
"""

def getPicture(url):
    resp = urllib.request.urlopen(url)
    #soup = BeautifulSoup(resp, 'lxml')
    soup = BeautifulSoup(resp)
    #print (soup)
    pattern = re.compile("data-original")
    for tag in soup.find_all(re.compile("^img")):
        #print (tag.attrs)
        #print (tag.attrs['src'])
        #print (tag.attrs['data-original'])
        #print (re.search(pattern, str(tag.attrs)))

        if re.search(pattern, str(tag.attrs)):
            print (tag.attrs['data-original'])
"""
        if tag.attrs['src'] == re.compile("$.gif"):
            print (tag.attrs['data-original'])
        else:
            print (tag.attrs['src'])
"""

if __name__ == "__main__":
    #url = input("Input the img address: ")
    url = "http://www.pop-fashion.com/patterns/graphics/"
    #url = ""
    getPicture(url)
