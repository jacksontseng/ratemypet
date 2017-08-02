import jinja2
import os
import webapp2
from google.appengine.ext import ndb
import datetime
import logging
import mimetypes

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
        age = int(self.request.get("age"))
        date = self.request.get("time_posted")
        picture = self.request.get("pic")
        file_name = self.request.get("file_name")

        new_pet(petname, atype, breed, description,age, date, picture, file_name)
        self.response.out.write("You have submitted your pet <br>")
        self.response.out.write("skdjglkjsadf")



        # self.redirect('/')


class AddPet2DS(ndb.Model):
    petname = ndb.StringProperty()
    atype = ndb.StringProperty()
    breed = ndb.StringProperty()
    time_posted = ndb.DateTimeProperty()
    description = ndb.StringProperty()
    age = ndb.IntegerProperty()
    picture = ndb.BlobProperty()
    file_name = ndb.StringProperty()

    # add image here



    def get(self):
        # why does it need ex - ?id=2ay and not just /2ay
        pic_file = self.request.get("name")
        query = AddPet2DS.query(AddPet2DS.file_name == pic_file)
        result = query.get()
        logging.info("It works ")

        if result:
            self.response.headers[b'Content-Type'] = mimetypes.guess_type(result.file_name)[0]
            self.response.write(result.blob)



def new_pet(petname, atype, breed, description, age, time_posted, picture, file_name): #add image argument
        """Puts a new pet into Datastore."""
        newpet = AddPet2DS(petname=petname, age=age, atype=atype, time_posted=datetime.datetime.now(), breed=breed, description = description, picture = picture, file_name=file_name)
        return newpet.put()

#logging.info(AddPet2DS.query().get())
#print AddPet2DS.query().get()
