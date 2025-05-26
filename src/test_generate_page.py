import unittest

from generate_page import extract_title


class TestGeneratePage(unittest.TestCase):
	def test_extract_title(self):
		markdown1 = "# Hello"
		title = extract_title(markdown1)
		self.assertEqual(title, 'Hello')

		markdown2 = """
		# Welcome
		
		In this program, we are going to...
		Thanks for your attention.
		"""
		self.assertEqual(extract_title(markdown2), 'Welcome')



if __name__ == '__main__':
	unittest.main()