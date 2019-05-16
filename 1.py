import urllib.request

import requests


def get_path_to_file():
    return "/home/pyatka_jeka/comicses-links"


def main():
    with open(get_path_to_file(), "r") as f:
        #TODO: readlines
        links = f.readline().split(" - ")
    i = 0
    url = links[0][0:len(links[0]) - 1]
    end_page_prepare = links[1].split("/")
    end_page = end_page_prepare[-1]
    #TODO: for
    while i < int(end_page):
        i += 1
        page_request = requests.get(url + str(i))
        page_source_content = page_request.text
        arr_with_content = page_source_content.split(" ")
        image_link = find_link_for_image(arr_with_content)
        download_image(image_link)


def find_link_for_image(page_content):
    i = 0
    index_of_the_link = 0
    #TODO: change to .find()
    for x in page_content:
        i += 1
        if x == "id=\"mainImage\"":
            index_of_the_link = i
    first_part = page_content[index_of_the_link]
    image_link = "https://acomics.ru/" + first_part[6:len(first_part) - 1]
    return image_link


def download_image(image_link):
    urllib.request.urlretrieve(image_link, "/home/pyatka_jeka/comicses_images/" + image_link.split('/')[-1])


if __name__ == "__main__":
    main()
