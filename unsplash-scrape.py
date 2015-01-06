#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import urllib 
import random

def unsplash_scrape ():
	url = "http://unsplash.com"
	r = requests.get(url)
	soup = BeautifulSoup(r.content)
	print ("Fetching images from unsplash.com:")
	for url in soup.find_all("img"):
		name = random.randrange(1,1000000)
		full_name = str(name) + ".jpg"
		uri = url.get("src")
		print uri 
		if uri == 0:
			print "No URL to retrieve"
		else:
			urllib.urlretrieve(uri,full_name)
	print("Done!")
unsplash_scrape()