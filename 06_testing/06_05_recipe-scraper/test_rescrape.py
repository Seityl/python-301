# Write a unittest test suite to test the rescrape module

import unittest
import rescrape

class TestRescrape(unittest.TestCase):
    def test_get_page_content(self):
        self.assertTrue(rescrape.get_page_content(self))
    def test_get_html_content(self):
        self.assertTrue(rescrape.get_html_content(self))
    def test_make_soup(self):
        self.assertTrue(rescrape.make_soup(self))
    def test_get_recipie_links(self):
        self.assertTrue(rescrape.get_recipie_links(self))
    def test_get_author(self):
        self.assertTrue(rescrape.get_author(self))
    def test_get_recipie(self):
        self.assertTrue(rescrape.get_recipie(self))

if __name__ == "__main__":
    unittest.main()
