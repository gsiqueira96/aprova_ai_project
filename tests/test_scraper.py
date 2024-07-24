import unittest
from webscraping.scraper import WebScraper


class TestWebScraper(unittest.TestCase):

    def setUp(self):
        self.scraper = WebScraper(base_url="http://example.com")

    def test_scraper_initialization(self):
        self.assertEqual(self.scraper.base_url, "http://example.com")

    def test_scrape_data(self):
        data = self.scraper.scrape("/test-page")
        self.assertIsNotNone(data)
        self.assertIn("expected_key", data)


if __name__ == "__main__":
    unittest.main()
