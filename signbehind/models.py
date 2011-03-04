from google.appengine.ext import db


class Profile(db.Model):
    ''' Represents a instagram user
    '''
    full_name = db.StringProperty()
    ig_user_id = db.StringProperty()
    ig_username = db.StringProperty()
    ig_access_token = db.StringProperty()

    def is_connected(self):
        ''' Checks if the user is currently connected

        :returns: True if connected, False otherwise
        '''
        return (self.ig_access_token and self.ig_user_id)
