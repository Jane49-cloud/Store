from django.test import TestCase


class TestcaseView(TestCase):
    def home_page_working(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("response", 'home.html')
        self.assertContains("response" 'hello')


class TestcaseViewTwo(TestCase):
    def test_the_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
        self.assertContains(response, "welcome")


