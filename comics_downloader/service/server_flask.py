from flask import Flask, request
from comics_downloader.script import launch_downloader

app = Flask(__name__)


@app.route("/", methods=['POST'])
def get_link():
    link = request.get_data()
    launch_downloader.get_url_to_comics_page(link)


if __name__ == "__main__":
    app.run()
