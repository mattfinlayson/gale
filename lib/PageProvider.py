#!/usr/bin/python

import os
import markdown
import string
import datetime

class PageProvider:
	def __init__(self):
		self.path = "/home/matt/gale/pages"
		self.list = os.listdir(self.path)
		self.list = sorted(self.list, reverse=True)
		self.parser = {
            "title":"",
            "date":"",
            "tags":"",
            "slug":"",
            "old_url":"",
            "new_url":"",
			"content_type":"" }
		self.parsed_list = []
		for article in self.list:
			self.parsed_list.append(self.parse_article(article, self.parser))	

	def fetch_one(self, new_url):
		dummy_article = self.parser
		dummy_article["body"] = "Not Found"
		dummy_article["title"] = "NotFound"
		dummy_article["date"] = "No Date"

		print new_url
		print 
		for article in self.parsed_list:
			print article["new_url"]
			if article["new_url"] == new_url:
				return article
		return dummy_article

	def parse_article(self, article, parser):
		f = open(os.path.join(self.path, article))
		text = f.readlines()
		parsed_article = {}
		for line in text:
			for key in parser:
				if key + ': ' in line:
					parsed_article[key] = line.replace(key + ': ','').replace('\n','') 
		parsed_article["body"] = ''.join(text[8:])
		words = string.split(parsed_article["body"])
		parsed_article["word_count"] = len(words)
		return parsed_article
