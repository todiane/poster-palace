from django.test import TestCase

# Create your tests here.

class IndexPageTest(TestCase):
	def test_index_page_returns_correct_response(self):
		response = self.client.get('/')

		self.assertTemplateUsed(response, 'home/index.html')
		self.assertEqual(response.status_code, 200)
        