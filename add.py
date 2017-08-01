import jinja2
import os
import webapp2
from google.appengine.ext import ndb
import datetime
import logging

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class AddPet(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/addpet.html')
        self.response.out.write(template.render())
    def post(self):
        petname = self.request.get("petname")
        atype = self.request.get("type")
        breed = self.request.get("breed")
        description = self.request.get("description")

        picture = self.request.get("pic")



        # self.redirect('/')


class AddPet2DS(ndb.Model):
    petname = ndb.StringProperty()
    atype = ndb.StringProperty()
    breed = ndb.StringProperty()
    time_posted = ndb.DateTimeProperty()
    description = ndb.StringProperty()

    # add image here


def new_pet(petname, atype, breed, description, age, time_posted, picture): #add image argument
  """Puts a new pet into Datastore."""
  newpet = AddPet2DS(petname=petname, age=age, atype=atype, time_posted=datetime.datetime.now(), breed=breed, description = description, picture = picture)
  return newpet.put()

logging.info(AddPet2DS.query().get())
print AddPet2DS.query().get()
