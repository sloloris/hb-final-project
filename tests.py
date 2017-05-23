""" Tests. """

import unittest
import os

import server
import server_functions

import model

class LoggedInTestCase(unittest.TestCase):
    """ Testing when user is logged in. """

    def setUp(self):
        self.client = server.app.test_client()
        server.app.config['TESTING'] = True

        # os.system('createdb testcontacts')
        model.connect_to_db(server.app, "postgresql:///testcontacts")
        model.fill_relationships_table()
        model.test_data()

        with self.client.session_transaction() as session:
            session['user_id'] = 1

    def tearDown(self):
        model.db.session.close()
        model.db.drop_all()
        # os.system('dropdb testcontacts')

    def test_index(self):
        result = self.client.get('/', follow_redirects=True)

        self.assertIn('<div class="sidenav">', result.data)
        self.assertNotIn('<div class="topnav" id="landing-nav">', result.data)
        
class LoggedOutTestCase(unittest.TestCase):
    """ Testing when user is logged out. """

    def setUp(self):
        self.client = server.app.test_client()
        server.app.config['TESTING'] = True

    def test_index(self):
        result = self.client.get('/', follow_redirects=True)

        self.assertIn('https://accounts.google.com/o/oauth2/v2/auth?scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.compose+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.labels+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.modify+https%3A%2F%2Fwww.google.com%2Fm8%2Ffeeds%2F+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcontacts.readonly+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&amp;redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Foauthcallback&amp;response_type=code&amp;client_id=1031894893410-0e7i2f7kaoenh6s9htvvm3mb1cab1trc.apps.googleusercontent.com&amp;access_type=offline', result.data)
        self.assertNotIn('<div class="sidenav">', result.data)



if __name__ == "__main__":
    unittest.main()