from urllib.request import urlopen
import json


def get_applist(url: str):
    result = json.loads(urlopen(url).read())

    return result["apps"]
