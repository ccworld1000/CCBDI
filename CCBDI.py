#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  CCBDI.py
#  
#  Copyright 2017 youhua deng (deng you hua | CC) <ccworld1000@gmail.com>
#  https://github.com/ccworld1000/CCBDI
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import re
import json
import requests

def getContent (url) :
	try :
		headers = { 'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
		r = requests.get (url, headers = headers)
		r.encoding = r.apparent_encoding
		content = r.text
		
		return content
		
	except Exception, e:
		print e.message
		return ""

def parseStockCode (url) :
	try :
		html = getContent (url)
		
		pattern = re.compile (r'var defData = {pages:8,data:(.*)?};', flags = re.M)
		out = pattern.search (html)

		g1 = out.group(1)
		
		items = json.loads(g1)
		
		#print (type (items))
		#print items;
		
		count = 1
		for item in items :
			#print item
			
			id = item['ID']
			Name = item['Name']
			DATADATE = item['DATADATE']
			VALUE = item['VALUE']
			
			print str(count) + " " + DATADATE + " " + str(VALUE)
			count = count + 1
		
	except Exception, e: 
		print e.message


