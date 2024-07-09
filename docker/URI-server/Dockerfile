FROM python:3.9-slim

WORKDIR /app

# 必要なパッケージをインストール
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# アプリケーションファイルをコピー
COPY app.py app.py

# Flaskサーバーを起動
CMD ["python", "app.py"]
