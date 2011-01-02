#!/usr/bin/python

import os
import tornado.httpserver
import tornado.ioloop
import tornado.web

import sys
sys.path.append("lib")

from ArticleProvider import ArticleProvider

class MainHandler(tornado.web.RequestHandler):
	def initialize(self):
		self.a = ArticleProvider()

	def get(self):
		self.render("templates/index.html", title="index", items=self.a.parsed_list)

class ArticleHandler(tornado.web.RequestHandler):
	def initialize(self):
		self.a = ArticleProvider()

	def get(self, new_url):
		article = self.a.fetch_one(new_url)
		#self.write(new_url + article["body"])
		self.render("templates/article.html", title=article["title"], item=article)

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "login_url": "/login",
    "xsrf_cookies": True,
}

application = tornado.web.Application([
	(r"/", MainHandler),
	(r"/article/([0-9]+/[0-9]+/[0-9]+/[-a-z]+/)", ArticleHandler),
], **settings)

if __name__ == "__main__":
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
