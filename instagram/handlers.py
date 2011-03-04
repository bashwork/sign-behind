from google.appengine.ext import webapp
from signbehind.models import Profile
from lib.lilcookies import LilCookies as Cookies
from instagram.client import InstagramAPI as Client
import settings

__api = Client(**settings.INSTAGRAM_SETTINGS)

class InstagramAuthHandler(webapp.RequestHandler):
    ''' Handler for connecting a user to the instagram session

    :uri: ../instagram/auth
    '''
    def get(self):
        self.redirect(__api.get_authorize_url())

class InstagramDisconnectHandler(webapp.RequestHandler):
    ''' Handler for disconnecting a user from their instagram
    connection.

    :uri: ../instagram/disconnect
    :cookie ig_user_id: The instagram user identifier
    '''
    def get(self):
        cookie = Cookies(self, settings.COOKIE_SECRET)
        id = cookie.get_secure_cookie(name = "ig_user_id")
        profile = Profile.all().filter('ig_user_id =', id).get()

        if profile: profile.delete()
        self.redirect('/')

class InstagramCallbackHandler(webapp.RequestHandler):
    ''' Handler for processing
    '''
    def get(self):
        code = self.request.get('code')
        token = __api.exchange_code_for_access_token(code)
        if not token: self.redirect('/error')

        client = Client(access_token=token)
        user = client.user('self')
        profile = Profile.all().filter('ig_user_id = ', user.id)
        profile = (profile.get() or Profile())

        profile.full_name = (user.fullname or user.username)
        profile.ig_user_id = user.id
        profile.ig_username = user.username
        profile.ig_access_token = access_token
        profile.put()

        cookie = Cookies(self, settings.COOKIE_SECRET)
        cookie.set_secure_cookie(name = 'ig_user_id',
            value = user.id, expires_days = 365)

        self.redirect('/connect')
