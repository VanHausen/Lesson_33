'''from django.test import TestCase

class TestCore1(TestCase):

    def test_signup(self):
        response = self.client.get('signup/')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_profile(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)

    def test_update_password(self):
        response = self.client.get('/update_password/')
        self.assertEqual(response.status_code, 200)'''
