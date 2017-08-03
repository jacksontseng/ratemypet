import jinja2
import os
import webapp2
from google.appengine.ext import ndb
from google.appengine.api.images import get_serving_url
from google.appengine.api import users

import logging
import add
import datetime

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class mainFeedHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
            greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
                nickname, logout_url)
            template = jinja_env.get_template('templates/feed.html')
            # if self.request.get('filter') == 'highest_rated':
            #     pets = highest_rated()

            if self.request.get('filter') == 'mostrecent':
                pets = mostrecent()

            elif self.request.get('filter') in ['dog', 'cat', 'bird', 'pig']:
                pets = atype(self.request.get('filter'))

            elif self.request.get('filter') == 'highest_rated':
                pets = get_top_ten()
            else:
                pets = allpets()
        # template = jinja_env.get_template('templates/feed.html')
        # if self.request.get('filter') == 'highest_rated':
        #     pets = get_top_ten()
        #
        # elif self.request.get('filter') == 'mostrecent':
        #     pets = mostrecent()
        #
        # elif self.request.get('filter') in ['dog', 'cat', 'bird', 'pig']:
        #     pets = atype(self.request.get('filter'))
        #
        # elif self.request.get('filter') == 'highest_rated':
        #     pets = get_top_ten()
        # else:
        #     pets = allpets()

        # pets = [i.to_dict() for i in pets]
        # for pet in pets:
        #     pet_key = get_serving_url(pet["picture"])


            args = {'pets': pets}
            self.response.write(template.render(args))

        # result =
        # self.response.headers['Content-Type'] = 'image/png'
        # for pet in pets:
        #     self.response.out.write(pet["picture"])
        #     self.response.out.write(pet["petname"])
        else:
            login_url = users.create_login_url('/')
            greeting = '<a href="{}">Sign in</a>'.format(login_url)

        self.response.write(
            '<html><body>{}</body></html>'.format(greeting))

# Create a new handler which it's only purpose is to
# return an image

def allpets():
    query = add.AddPet2DS.query()
    fetch = query.fetch()
    logging.info(query)
    return fetch


def mostrecent():
    """Fetches all GIFs posted in the past hour."""
    onedayago = datetime.datetime.now() - datetime.timedelta(hours=24)
    query = add.AddPet2DS.query(add.AddPet2DS.time_posted > onedayago)
    return query.fetch(limit=10)




def atype(animal_type):
    print animal_type
    query = add.AddPet2DS.query().filter(ndb.GenericProperty('atype') == animal_type)
    animalfilter = query.fetch(limit = 10)
    print animalfilter
    return animalfilter

def get_top_ten():
  """Fetches the top ten ranked Bieber GIFs."""
  query = add.AddPet2DS.query().order(-add.AddPet2DS.votes)
  logging.info(query.fetch(limit=10))
  return query.fetch(limit=10)

def upvote(petname):
  """Upvotes the given Bieber GIF."""
  query = add.AddPet2DS.query(add.AddPet2DS.petname == petname)
  result = query.get()
  if result:
    if not result.votes:
      result.votes = 1
    else:
      result.votes += 1
    result.put()
    return result

class UpvoteHandler(webapp2.RequestHandler):
    """Registers a vote for a Bieber GIF."""

    def post(self):
        petname = self.request.get('petname')
        updated_entity = upvote(petname)
        print updated_entity
