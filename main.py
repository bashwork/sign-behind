from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from signbehind.models import IndexHandler, ConnectHandler
from instagram.models import *

#---------------------------------------------------------------------------#
# Route Configuration
#---------------------------------------------------------------------------#
application = webapp.WSGIApplication([
    ('/', IndexHandler),
    ('/connect', ConnectHandler),
    ('/instagram/auth', InstagramAuthHandler),
    ('/instagram/disconnect', InstagramDisconnectHandler),
    ('/instagram/callback', InstagramCallbackHandler),
    ], debug=True)

#---------------------------------------------------------------------------#
# Main Loader
#---------------------------------------------------------------------------#
def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
