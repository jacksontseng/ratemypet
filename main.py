#!/usr/bin/env python

import webapp2
import jinja2
import os
import json
from google.appengine.api import users
import add
import logging
import add
import shutil




jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/main.html')
        return self.response.write(template.render())

class signin(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
            greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
                nickname, logout_url)
        else:
            login_url = users.create_login_url('/')
            greeting = '<a href="{}">Sign in</a>'.format(login_url)

        self.response.write(
            '<html><body>{}</body></html>'.format(greeting))

class ImageHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/feed.html')
        return self.response.write(template.render())


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/signin', signin),
    ('/image', ImageHandler),
    ('/addpet', add.AddPet),
], debug=True)
