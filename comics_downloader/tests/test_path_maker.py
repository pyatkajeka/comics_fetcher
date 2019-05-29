import unittest
from comics_downloader.core import path_maker


class PathMakerTest(unittest.TestCase):
    def test_comics_name(self):
        self.assertEqual("good-saddle", path_maker.make_comics_name("https://acomics.ru/~good-saddle/234"),
                         "Wrong name")

    #def test_create_folder(self):
     #   pass

    def test_make_dictionary(self):
        test_list =  ['https://acomics.ru/~good-saddle/ -  https://acomics.ru/~good-saddle/245\n',
                        'https://acomics.ru/~Cats-Cafe/ - https://acomics.ru/~Cats-Cafe/160\n']
        test_dict = {'https://acomics.ru/~good-saddle/': '245', 'https://acomics.ru/~Cats-Cafe/': '160'}
        self.assertEqual(test_dict, path_maker.make_dictionary(test_list), "Wrong format of the dictionary")


if __name__ == "__main__":
    unittest.main()
