from google.appengine.ext import webapp
from signbehind.models import Profile
from lib.lilcookies import LilCookies as Cookies
import settings


class IndexHandler(webapp.RequestHandler):
    ''' The main landing page

    :uri: ../
    :cookie ig_user_id: The instagram user identifier
    '''
    def get(self):
        cookie = Cookies(self, settings.COOKIE_SECRET)
        id = cookie.get_secure_cookie(name = "ig_user_id")
        profile = Profile.all().filter('ig_user_id =', id).get()
        context  = {}

        if profile and profile.is_connected():
            template = 'connected.html'
            context  = {
                'profile': profile,
                'ig_user_id': id,
            }
        else: template = 'disconnected.html'
        self.render_template(template, context)


class ConnectHandler(webapp.RequestHandler):
    ''' The main connection handler

    :uri: ../connect
    :cookie ig_user_id: The instagram user identifier
    '''
    def get(self):
        cookie = Cookies(self, settings.COOKIE_SECRET)
        id = cookie.get_secure_cookie(name = "ig_user_id")
        profile = Profile.all().filter('ig_user_id =', id).get()

        if profile and profile.is_connected():
            self.redirect('/')
        else: self.redirect('/instagram/auth')
