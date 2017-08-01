import jinja2
import os
import webapp2
from google.appengine.ext import ndb
import logging
import add
import datetime

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class mainFeedHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/feed.html')
        if self.request.get('filter') == 'highest_rated':
            pets = highest_rated()

        elif self.request.get('filter') == 'mostrecent':
            pets = mostrecent()

        elif self.request.get('filter') in ['dog', 'cat', 'bird', 'pig']:
            pets = atype(self.request.get('filter'))

        else:
            pets = allpets()


        args = {'pets': pets}

        self.response.write(template.render(args))


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


def highest_rated():
    pass

def atype(animal_type):
    print animal_type
    query = add.AddPet2DS.query().filter(ndb.GenericProperty('atype') == animal_type)
    animalfilter = query.fetch(limit = 10)
    print animalfilter
    return animalfilter
