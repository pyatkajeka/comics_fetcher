import os
import re


def make_dictionary(list_with_links):
    links = list(map(lambda x: x.replace('\n', '').split(' - '), list_with_links))
    dict_with_comicses_links = {
        left_link: re.search("([0-9]+)$", right_link.strip()).group(1)
        for left_link, right_link in links
    }
    return dict_with_comicses_links


def make_comics_name(link_string):
    comics_name_start_index = link_string.find('~') + 1
    comics_name_end_index = link_string[comics_name_start_index:].find('/')
    comics_name = link_string[comics_name_start_index:][:comics_name_end_index]
    return comics_name


def create_folder(comics_name):
    path = "/home/pyatka_jeka/" + comics_name
    if os.path.exists(path):
        pass
    else:
        try:
            os.mkdir(path)
        except OSError:
            print(f"Creation of the directory {path} failed")