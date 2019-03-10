#!/usr/bin/python
## -#*- coding: utf8 -*-#

import urllib2
import os

lststr = open('list.txt', 'r')

lst = lststr.readlines()

dldir = "./images/"

lststr.close()

for url in lst:
    q = urllib2.Request(url)
    # i'm white rat
    q.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36')
    f = urllib2.urlopen(q) 
    with open(dldir + os.path.basename(url), "wb") as code:
        code.write(f.read())
