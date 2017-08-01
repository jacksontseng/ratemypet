import jinja2
import os
import webapp2
from google.appengine.ext import ndb
import datetime
import add
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
        img_id = self.request.get("image-id")
        # add image url here

        new_pet(petname, atype, breed, description, picture) #add image argument
        self.response.out.write("You have submitted your pet")
        # self.redirect('/')


class AddPet2DS(ndb.Model):
    petname = ndb.StringProperty()
    atype = ndb.StringProperty()
    breed = ndb.StringProperty()
    time_posted = ndb.DateProperty()
    description = ndb.StringProperty()
    picture = ndb.BlobProperty()


#def getPicturesOfFluffy(self):
    # This is a query
#    query = AddPet2DS.query(AddPet2DS.atype == 'dog')

    # THESE are the results
#    results = query.fetch(20)

#    images = []
#    for result in results:
#        images.append(result.picture)



#class Image(ndb.Model):
#    Image.query
    #img_id = randint(0,1000000000000)
    # add image here


def new_pet(petname, atype, breed, description, picture):     #add image argument
    """Puts a new pet into Datastore."""
    newpet = AddPet2DS(petname=petname, atype=atype, time_posted=datetime.datetime.now(), breed=breed, description = description, picture= picture)
    new_key = newpet.put()
    logging.info(new_key)
