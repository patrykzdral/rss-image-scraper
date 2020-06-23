from bs4 import BeautifulSoup

import requests
import shutil
import re


def download_nyt_image(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    aasClass1 = soup.find_all("img")
    pattern = re.compile("^css-.*$")
    image_info = []
    for a in aasClass1:
        photoWithClass = ""
        try:
            photoWithClass = a["class"][0]
        except Exception:
            photoWithClass = ''

        if pattern.match(photoWithClass):
            try:
                image_info.append((a["src"], a['alt']))
            except Exception:
                image_info.append((a["src"], "default"))
    return (image_info[:1] or [None])[0]
