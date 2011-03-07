import os
from google.appengine.ext.webapp import RequestHandler, template
from signbehind.models import Profile
from lib.lilcookies import LilCookies as Cookies
import settings


class BaseRequestHandler(RequestHandler):
    ''' A base request handler to add all utility methods
    not supplied by the GAE environment
    '''

    def render_template(self, file, context):
        ''' A helper method to make rendering templates easier

        :param file: The template to render
        :param context: The data context to pass to the template
        '''
        context = context or {}
        path = os.path.join(os.path.dirname(__file__), 'templates', file)
        self.response.out.write(template.render(path, context))

class IndexHandler(BaseRequestHandler):
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


class ConnectHandler(BaseRequestHandler):
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
