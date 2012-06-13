#!/usr/bin/python
# -*- coding: utf-8 -*-

import simplejson as json
import urllib
import sys

username = "mattfinlayson"
tag1 = "python"
tag2 = "supervisor"
tag3 = "tornado"
tags = ["python", "supervisor", "tornado"]
items = [0, 1, 2]

base_url = "http://feeds.pinboard.in/json/v1/u:%s" % (username)

for tag in tags:
	target_url = "%s/t:%s" % (base_url, tag)
	print target_url
	result = json.load(urllib.urlopen(target_url))
	try:
		for item in items:
			for k, v in result[item].iteritems():
				print k, v.encode('utf-8')
	except IndexError:
		pass
