import sys
from comics_downloader.core import (
    path_maker,
    fetcher,
)


def get_path_to_file():
    if len(sys.argv) == 1:
        return "/home/pyatka_jeka/comicses-links"
    else:
        return str(sys.argv[1])


def main():
    with open(get_path_to_file(), "r") as f:
        links_new = f.readlines()
    dict_with_links = path_maker.make_dictionary(links_new)
    for link, end_page in dict_with_links.items():
        curr_comics_name = path_maker.make_comics_name(link)
        path_maker.create_folder(curr_comics_name)
        for i in range(int(end_page)):
            page_source_content = fetcher.page_source_request(link, i)
            image_link = fetcher.find_link_for_image(page_source_content)
            fetcher.download_image(image_link, curr_comics_name)


if __name__ == "__main__":
    main()
