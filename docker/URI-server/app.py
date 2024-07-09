from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# ホストマシンの画像ディレクトリへのパスを設定
IMAGE_DIR = '/host_images'

@app.route('/images/<filename>')
def get_image(filename):
    return send_from_directory(IMAGE_DIR, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
