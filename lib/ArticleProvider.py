#!/usr/bin/python

import os
import markdown
import string
import datetime

class ArticleProvider:
	def __init__(self):
		self.path = "/home/matt/gale/articles"
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

	def latest(self):
		return self.parse_article(self.list_one(), self.parser)

	def list_one(self):
		return self.list[0]

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
		
	def pub_dates(self):
		days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
		months = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
		for article in self.parsed_list:
			year, month, day = article["date"].split("/")
			pub_date = datetime.date(int(year), int(month), int(day))
			article["date"] = "%s, %s %s %s 00:00:01 GMT" % (days[pub_date.weekday()], pub_date.day, months[pub_date.month], pub_date.year)

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
