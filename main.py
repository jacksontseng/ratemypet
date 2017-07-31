#!/usr/bin/env python

import webapp2
import jinja2
import os
import json
from google.appengine.api import users
import add
import logging



jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/main.html')
        return self.response.write(template.render())

class signin(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        template = jinja_env.get_template('templates/signin.html')
        self.response.out.write(template.render())

        if user:
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
            greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
                nickname, logout_url)
        else:
            login_url = users.create_login_url('/')
            greeting = '<a href="{}">Sign in</a>'.format(login_url)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/signin', signin),
    ('/addpet', add.addPet)
], debug=True)
