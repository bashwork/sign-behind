from google.appengine.ext import webapp
from signbehind.models import Profile
import settings


class MainHandler(webapp.RequestHandler):
    ''' The main landing page

    :uri: ../
    '''
    def get(self):
        id = cookie.get(name="ig_user_id")
        profile = Profile.all().filter('ig_user_id =', id).get()
        if profile.is_connected():
        else 'disconnected.html'
        self.render_template(template)

class ConnectHandler(webapp.RequestHandler):
    ''' The main connection handler

    :uri: ../connect
    '''
    def get(self):
        id = cookie.get(name="ig_user_id")
        profile = Profile.all().filter('ig_user_id =', id).get()
        if profile.is_connected():
        else 'disconnected.html'
        self.render_template(template)
