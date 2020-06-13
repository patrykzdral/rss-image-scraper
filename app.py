from flask import Flask, jsonify
from flask import request

from bbc import download_bbc_image
from cnn import download_cnn_image
from new_york_times import download_nyt_image

app = Flask(__name__)


@app.route('/get-nyt-image', methods=['POST'])
def get_nyt_image():
    data = request.get_json(silent=True)
    img = download_nyt_image(data['url'])
    if img is not None:
        return jsonify(
            src=img[0],
            title=img[1]
        )
    else:
        return jsonify()


@app.route('/get-bbc-image', methods=['POST'])
def get_bbc_image():
    data = request.get_json(silent=True)
    img = download_bbc_image(data['url'])
    if img is not None:
        return jsonify(
            src=img[0],
            title=img[1]
        )
    else:
        return jsonify()


@app.route('/get-cnn-image', methods=['POST'])
def get_cnn_image():
    data = request.get_json(silent=True)
    img = download_cnn_image(data['url'])
    if img is not None:
        return jsonify(
            src=img[0],
            title=img[1]
        )
    else:
        return jsonify()


if __name__ == '__main__':
    app.run()
