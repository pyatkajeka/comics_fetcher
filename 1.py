import urllib.request
import re
import os
import requests


def get_path_to_file():
    return "/home/pyatka_jeka/comicses-links"

#TODO: make it asyncio

def main():
    with open(get_path_to_file(), "r") as f:
        links_new = f.readlines()
    dict_with_links = makeDictionary(links_new)
    for x in dict_with_links:
        curr_comics_name = make_comics_name(x)
        create_folder(curr_comics_name)
        for i in range(int(dict_with_links[x])):
            page_source_content = page_source_request(x, i)
            image_link = find_link_for_image(page_source_content)
            download_image(image_link, curr_comics_name)


def find_link_for_image(page_content):
    second_part_address = re.search('id=\"mainImage\" src=\"([^\"]+)\"', page_content).group(1)
    image_link = "https://acomics.ru/" + second_part_address
    return image_link


def page_source_request(string_with_link, counter):
    page_request = requests.get(string_with_link + str(counter))
    page_source_content = page_request.text
    return page_source_content


def makeDictionary(list_with_links):
    links = list(map(lambda x: x.replace('\n', ''), list_with_links))
    dict_with_comicses_links = {}
    for x in links:
        splitted_links = x.split(" - ")
        dict_with_comicses_links[splitted_links[0]] = splitted_links[1]
    for x in dict_with_comicses_links:
        end_page_number = re.search("([0-9]+)$", dict_with_comicses_links[x].strip()).group(1)
        dict_with_comicses_links[x] = end_page_number
    return dict_with_comicses_links


def make_comics_name(link_string):
    comics_name_start_index = link_string.find('~') + 1
    comics_name_end_index = link_string[comics_name_start_index:].find('/')
    comics_name = link_string[comics_name_start_index:][:comics_name_end_index]
    return comics_name


def download_image(image_link, comics_name):
    urllib.request.urlretrieve(image_link, "/home/pyatka_jeka/" + comics_name + "/" + image_link.split('/')[-1])


def create_folder(comics_name):
    path = "/home/pyatka_jeka/" + comics_name
    if os.path.exists(path):
        pass
    else:
        try:
            os.mkdir(path)
        except OSError:
            print("Creation of the directory %s failed" % path)


if __name__ == "__main__":
    main()
