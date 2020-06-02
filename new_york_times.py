from bs4 import BeautifulSoup

import requests
import shutil
import re


def download_image(image):
    response = requests.get(image[0], stream=True)
    realname = ''.join(e for e in image[1] if e.isalnum())

    file = open("C://images//new-york-times//{}.jpg".format(realname), 'wb')

    response.raw.decode_content = True
    shutil.copyfileobj(response.raw, file)
    del response


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
        except KeyError:
            photoWithClass = ''

        if pattern.match(photoWithClass):
            try:
                image_info.append((a["src"], a['alt']))
            except KeyError:
                image_info.append((a["src"], "default"))
    return (image_info[:1] or [None])[0]
