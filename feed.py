import jinja2
import os
import webapp2
from google.appengine.ext import ndb
import add
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class all(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/feed.html')
        self.response.out.write(template.render())
        query = add.AddPet2DS.query().get()
