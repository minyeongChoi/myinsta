from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기

app = Flask(__name__)

@app.route('/')
def home():  # 함수명 수정 - 이름만 보고 접속되는 페이지를 확인할 수 있게!
    return render_template('index.html')


@app.route('/mypage')
def posting():
    return render_template('posting.html')


# flask를 실행 시켜주는 공간
if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)