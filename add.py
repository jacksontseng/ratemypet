import jinja2
import os
import webapp2
import image


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class addPet(webapp2.RequestHandler):
    def post(self):

        myImage = Image.open("your_image_here")
        myImage.show()



app = webapp2.WSGIApplication([
    ('/addpet', addPet)
], debug=True)
