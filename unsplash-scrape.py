#!/usr/bin/env python
#-*- coding: utf-8 -*-
import re
import sys
import urllib

#artwork
print "                       _           _"
print " _   _ _ __  ___ _ __ | | __ _ ___| |__"
print "| | | | '_ \/ __| '_ \| |/ _` / __| '_ \ "
print "| |_| | | | \__ \ |_) | | (_| \__ \ | | |"
print " \__,_|_| |_|___/ .__/|_|\__,_|___/_| |_|"
print "                |_|                    "


#Enter the URL that you wish to scrape the shit out of.
sampleUrl = "http://unsplash.com"
urlAddInfo = urllib.urlopen(sampleUrl)
data = urlAddInfo.read()

#Sample extensions we'll be looking for: pngs and pdfs
TARGET_EXTENSIONS = "(jpg)"
targetCompile = re.compile(TARGET_EXTENSIONS, re.UNICODE|re.MULTILINE)

#Let's get all the urls: match criteria{no spaces or " in a url}
urls = re.findall('(https?://[^\s"]+)', data, re.UNICODE|re.MULTILINE)

#We want these folks
extensionMatches = filter(lambda url: url and targetCompile.search(url), urls)

#The rest of the unmatched urls for which the scrapping can also be repeated.
nonExtMatches = filter(lambda url: url and not targetCompile.search(url), urls)

print "√ Navigated to " + sampleUrl

def fileDl(targetUrl):
  #Function to handle downloading of files.
  #Arg: url => a String
  #Output: Boolean to signify if file has been written to memory

  #Validation of the url assumed, for the sake of keeping the illustration short
  urlAddInfo = urllib.urlopen(targetUrl)
  data = urlAddInfo.read()
  fileNameSearch = re.search("([^\/\s]+)$", targetUrl + ".jpg")#Text right before the last slash '/'
  if not fileNameSearch:
     sys.stderr.write("X Could not extract a filename from url '%s'\n"%(targetUrl))
     return False
  fileName = fileNameSearch.groups(1)[0]
  with open(fileName, "wb") as f:
    f.write(data)
    sys.stderr.write("√ Wrote %s to memory\n"%(fileName))
  return True

#Let's now download the matched files
dlResults = map(lambda fUrl: fileDl(fUrl), extensionMatches)
successfulDls = filter(lambda s: s, dlResults)
sys.stderr.write("Downloaded %d files from %s\n"%(len(successfulDls), sampleUrl))
