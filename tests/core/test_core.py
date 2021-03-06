from tests.client_base import ClientTestCase

class CoreTestCase(ClientTestCase):

    def test_core_index(self):
        resp = self.client.get('/')

        self.assertIn("zadacha", resp.get_data(as_text=True))
        self.assertIn("Sign Up", resp.get_data(as_text=True))

    def test_login_logout(self):
        u = self.addUser()
        resp = self.login(u.email, u.password)

        self.assertTrue("Sign Out" in resp.get_data(as_text=True))

        resp = self.logout()
        self.assertTrue("Sign In" in resp.get_data(as_text=True))