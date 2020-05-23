from flask import Flask, jsonify
from flask import request

from new_york_times import download_nyt_image

app = Flask(__name__)


@app.route('/get-image-photo-link', methods=['POST'])
def get_nyt_image():
    data = request.get_json(silent=True)
    print(data)
    img = download_nyt_image(data['url'])
    print(jsonify(img))
    if img is not None:
        return jsonify(
            src=img[0],
            title=img[1]
        )
    else:
        return jsonify()


if __name__ == '__main__':
    app.run()
