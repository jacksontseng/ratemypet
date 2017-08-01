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

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/home.html')
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

class Test(webapp2.RequestHandler):
    def save_uploaded_file (form_field, upload_dir):
        form = cgi.FieldStorage()
        if not form.has_key(form_field): return
        fileitem = form[form_field]
        if not fileitem.file: return

        outpath = os.path.join(upload_dir, fileitem.filename)

        with open(outpath, 'wb') as fout:
            shutil.copyfileobj(fileitem.file, fout, 100000)

    #def get(self):
        #myImage = Image.open("your_image_here")
        #myImage.show()

    #def post(self):
        #POST https://www.googleapis.com/upload/drive/v3?uploadType=media


app = webapp2.WSGIApplication([
    ('/main', MainHandler),
    ('/', HomeHandler),
    ('/signin', signin),
    ('/test', Test),
    ('/addpet', add.AddPet)
], debug=True)
