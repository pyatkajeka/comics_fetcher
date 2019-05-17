import urllib.request
import re

import requests


def get_path_to_file():
    return "/home/pyatka_jeka/comicses-links"


# TODO: func with the request to page source, remake download to different folders and for a several comicses


def main():
    with open(get_path_to_file(), "r") as f:
        links_new = f.readlines()
        makeDictionary(links_new)
    '''
    i = 0
    url = links[0][0:len(links[0]) - 1]
    end_page_prepare = links[1].split("/")
    end_page = end_page_prepare[-1]
    for i in range(int(end_page)):
        i += 1
        page_request = requests.get(url + str(i))
        page_source_content = page_request.text
        arr_with_content = page_source_content
        image_link = find_link_for_image(arr_with_content)
        download_image(image_link)
        '''


def find_link_for_image(page_content):
    second_part_address = re.search('id=\"mainImage\" src=\"([^\"]+)\"', page_content).group(1)
    image_link = "https://acomics.ru/" + second_part_address
    return image_link


def page_source_request(string_with_link):
    pass


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


def download_image(image_link):
    urllib.request.urlretrieve(image_link, "/home/pyatka_jeka/comicses_images/" + image_link.split('/')[-1])


if __name__ == "__main__":
    main()
