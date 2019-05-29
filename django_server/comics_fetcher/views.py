from django.shortcuts import render
from comics_downloader.script import launch_downloader
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def fetch_request(request):
    json_dict = json.loads(request.body)
    list_links = list(map(json_dict.get, json_dict))
    final_dict = {list_links[0]: list_links[1]}
    launch_downloader.loop_for_download(final_dict)
