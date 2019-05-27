import urllib.request
import re
import requests


def find_link_for_image(page_content):
    second_part_address = re.search('id=\"mainImage\" src=\"([^\"]+)\"', page_content).group(1)
    image_link = "https://acomics.ru/" + second_part_address
    return image_link


def page_source_request(string_with_link, counter):
    page_request = requests.get(string_with_link + str(counter))
    page_source_content = page_request.text
    return page_source_content


def download_image(image_link, comics_name):
    urllib.request.urlretrieve(image_link, "/home/pyatka_jeka/" + comics_name + "/" + image_link.split('/')[-1])
