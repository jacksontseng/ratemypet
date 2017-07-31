import jinja2
import os
import webapp2


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class addPet(webapp2.RequestHandler):
    def post(self):
        super(addPet, self).__init__()
        self.arg = arg
