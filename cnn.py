from bs4 import BeautifulSoup

import requests
import re


def download_cnn_image(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    aasClass1 = soup.find_all("img")
    pattern = re.compile("^media__image.*$")
    srcPattern = re.compile("^http.*$")
    srcPattern2 = re.compile("^//cdn.*$")
    image_info = []
    for a in aasClass1:
        photoWithClass = ""
        try:
            photoWithClass = a["class"][0]
            if srcPattern.match(a["src"]):
                return a["src"], a['alt']
            elif srcPattern2.match(a["src"]):
                removedSign = a["src"].replace("//", "http://", 1)
                return removedSign, a['alt']
        except Exception:
            photoWithClass = ''

        if pattern.match(photoWithClass):
            try:
                image_info.append((a["src-mini"], a['alt']))
            except Exception:
                image_info.append((a["src"], "default"))
    return (image_info[:1] or [None])[0]
