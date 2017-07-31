import jinja2
import os
import webapp2



jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class addPet(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/addpet.html')
        self.response.out.write(template.render())
    def post(self):


        #https://www.googleapis.com/upload/drive/v3?uploadType=media

        my_vars = {
            "petname":self.request.get("petname"),
            "type":self.request.get("type"),
            "breed":self.request.get("breed"),
            "description":self.request.get("description"),
            "show":self.request.get("show"),
            "fun":self.request.get("fun")
        }
        self.response.out.write("You have submitted your pet")



app = webapp2.WSGIApplication([
    ('/addpet', addPet)
], debug=True)
