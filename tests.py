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

        os.system('createdb testcontacts')
        model.connect_to_db(server.app, "postgresql:///testcontacts")
        model.fill_relationships_table()
        model.test_data()

        with self.client.session_transaction() as session:
            session['user_id'] = 1

    def tearDown(self):
        os.system('dropdb testcontacts')

    def test_index(self):
        result = self.client.get('/')

        self.assertIn('<div class="sidenav">', result.data)
        self.assertNotIn('<div class="topnav" id="landing-nav">', result.data)
        
class LoggedOutTestCase(unittest.TestCase):
    """ Testing when user is logged out. """

    def setUp(self):
        self.client = server.app.test_client()
        server.app.config['TESTING'] = True

    def test_index(self):
        result = self.client.get('/')

        self.assertIn('https://accounts.google.com/signin/oauth/oauthchooseaccount?client_id=1031894893410-0e7i2f7kaoenh6s9htvvm3mb1cab1trc.apps.googleusercontent.com&as=7e20c7a12da8bebd&destination=http%3A%2F%2Flocalhost%3A5000&approval_state=!ChRrSkpKVWRtOEI1ZGlGZk85T1EtaRIfYzBhM2xrclRDS0FUb1Bud0gtVkU1UUZHMGdOc3d4VQ%E2%88%99ADiIGyEAAAAAWSXc04-5axhkY-AJTOqqHCCsKwd8FTjK&xsrfsig=AHgIfE_XjrmCptD3FSQBqKcN_oj3T9rJJA&flowName=GeneralOAuthFlow', result.data)
        self.assertNotIn('<div class="sidenav">', result.data)



if __name__ == "__main__":
    unittest.main()