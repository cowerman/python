import urllib.request
import os
import re
import sys
import time
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

def getPicture(url, dir_file):
    i = 0
    page = 0
    last_page = 0
    path = './img/'+str(dir_file)+'/'

    # create directory to store img
    if not os.path.exists(''):
        os.makedirs(path)

    # pattern for find_all
    pattern = re.compile("data-original")
    pattern_next_page = re.compile("nextPage")
    while True:
        try:
            resp = urllib.request.urlopen(url)
        except:
            time.sleep(10)
            resp = urllib.request.urlopen(url)
        soup = BeautifulSoup(resp, 'lxml')
        #soup = BeautifulSoup(resp)
        #print (soup)
        print("=====================正在爬取第"+str(page+1)+"页=========")
        for tag in soup.find_all(re.compile("^img")):
            #print (tag.attrs['alt'], tag.attrs['src'])
            #print (tag.attrs['data-original'])
            #print (re.search(pattern, str(tag.attrs)))
            #print (tag.attrs['alt'], tag.attrs['src'])
            if re.search(pattern, str(tag.attrs)):
                conn = urllib.request.urlopen(str(tag.attrs['data-original']))
                print ('Download the %d picture...' % i)
                try:
                    f = open(str(path)+re.sub(r'[/ ]', '_', str(tag['alt']))+str(i)+".jpg", 'wb')
                except IOError:
                    print ('File not Exists')
                except:
                    f.close
                    break
                f.write(conn.read())
                f.close
                i += 1
    
            resp.close()

        page += 1

        for nextag in soup.find_all("a"):
            #print (nextag.attrs)
            if re.search(pattern_next_page, str(nextag.attrs)):
                #print (nextag.attrs['href'])
                url = nextag.attrs['href']

        if last_page == 1:
            print ("Complete the "+str(dir_file)+'!!!')
            break

if __name__ == "__main__":
    #url = input("Input the img address: ")
    url = "http://www.pop-fashion.com/patterns/graphics/"
    url1 = "http://www.pop-fashion.com/references/fabricgallery/"
    url2 = "http://www.pop-fashion.com/patterns/topbrands/"
    #url = ""
    #getPicture(url, 'graphics')
    #getPicture(url1, 'fabric_grallery')
    getPicture(url2, 'top_brands')
