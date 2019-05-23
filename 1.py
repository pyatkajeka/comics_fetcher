import urllib.request
import re
import os
import requests
import sys

def get_path_to_file():
    if (len(sys.argv) == 1):
        return "/home/pyatka_jeka/comicses-links"
    else:
        return str(sys.argv[1])


#TODO: make it asyncio
#TODO: make requirements.txt

def main():
    with open(get_path_to_file(), "r") as f:
        links_new = f.readlines()
    dict_with_links = make_dictionary(links_new)
    for link, end_page in dict_with_links.items():
        curr_comics_name = make_comics_name(link)
        create_folder(curr_comics_name)
        for i in range(int(end_page)):
            page_source_content = page_source_request(link, i)
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
            print(f"Creation of the directory {path} failed")


if __name__ == "__main__":
    main()
