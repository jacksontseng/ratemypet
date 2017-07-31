import jinja2
import os
import webapp2


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class addPet(webapp2.RequestHandler):
    def post(self):

        my_vars = {
            "noun1":self.request.get("noun1"),
            "activity":self.request.get("activity"),
            "celebrity":self.request.get("celebrity"),
            "teacher":self.request.get("teacher"),
            "show":self.request.get("show"),
            "fun":self.request.get("fun")
        }
        self.response.out.write("You have submitted your madlib")


app = webapp2.WSGIApplication([
    ('/addpet', addpet)
], debug=True)
