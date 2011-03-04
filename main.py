from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

#---------------------------------------------------------------------------#
# Route Configuration
#---------------------------------------------------------------------------#
application = webapp.WSGIApplication([
    ('/', MainHandler),
    ('/connect', ConnectHandler),
    ('/instagram/auth', InstagramAuth),
    ('/instagram/disconnect', InstagramDisconnect),
    ('/instagram/callback', InstagramCallback),
    ('/instagram/subscribe', InstagramSubscribe),
    ('/instagram/push_callback', InstagramPushCallback),
    ], debug=True)

#---------------------------------------------------------------------------#
# Main Loader
#---------------------------------------------------------------------------#
def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
