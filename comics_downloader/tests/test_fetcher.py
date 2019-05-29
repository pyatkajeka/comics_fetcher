import unittest
from comics_downloader.core import fetcher

class TestFetcher(unittest.TestCase):


    def fetch_test_source(self):
        path = "/home/pyatka_jeka/PycharmProjects/first_try/comics_downloader/tests/test_page_source.txt"
        with open(path, "r") as f:
            pg_source = f.readlines()
        test_pg_source = ''.join(pg_source)
        return test_pg_source

    def test_find_link_for_image(self):
        self.assertEqual(fetcher.find_link_for_image(self.fetch_test_source()),
                         "https://acomics.ru/upload/!c/Deer/whitewater/000001-n58yq3wk7v.jpg", "Not a link")


if __name__ == "__main__":
    unittest.main