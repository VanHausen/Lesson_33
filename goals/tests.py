'''from django.test import TestCase

class TestCore2(TestCase):

    def test_board_create(self):
        response = self.client.get('board/create')
        self.assertEqual(response.status_code, 200)

    def test_board_list(self):
        response = self.client.get('board/list')
        self.assertEqual(response.status_code, 200)

    def test_board_pk(self):
        response = self.client.get('board/<pk>')
        self.assertEqual(response.status_code, 200)

    def test_goal_category_create(self):
        response = self.client.get('goal_category/create')
        self.assertEqual(response.status_code, 200)

    def test_goal_category_list(self):
        response = self.client.get('goal_category/list')
        self.assertEqual(response.status_code, 200)

    def test_goal_category_pk(self):
        response = self.client.get('goal_category/<pk>')
        self.assertEqual(response.status_code, 200)

    def test_goal_create(self):
        response = self.client.get('goal/create')
        self.assertEqual(response.status_code, 200)

    def test_goal_list(self):
        response = self.client.get('goal/list')
        self.assertEqual(response.status_code, 200)

    def test_goal_pk(self):
        response = self.client.get('goal/<pk>')
        self.assertEqual(response.status_code, 200)

    def test_goal_comment_create(self):
        response = self.client.get('goal_comment/create')
        self.assertEqual(response.status_code, 200)

    def test_goal_comment_list(self):
        response = self.client.get('goal_comment/list')
        self.assertEqual(response.status_code, 200)

    def test_goal_comment_pk(self):
        response = self.client.get('goal_comment/<pk>')
        self.assertEqual(response.status_code, 200)'''