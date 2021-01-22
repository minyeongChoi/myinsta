from flask import Flask, render_template, jsonify, request
from datetime import date
import requests

from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.my_insta  # 'my_insta' 이름 db생성

@app.route('/' )
def home():  # 함수명 수정 - 이름만 보고 접속되는 페이지를 확인할 수 있게!
    return render_template('index.html')


## API 역할을 하는 부분
@app.route("/upload",methods=["POST"])
def write_review(): #데이터를 저장
    # Ajax를 통해서 flask로 들어온 form데이터 분리하기
    title = request.form['title']
    # photo = request.form['author']
    review = request.form['review']

    #review 가 문자열이면 날짜 출력..?
    if (str(type(review)) == "<class 'str'>"):
        day = str(date.today())

    #딕셔너리로 데이터 묶기
    review_data = {
        'title':title,
        # 'photo':photo,
        'review':review,
        'day':day
    }

    #mongodb로 데이터 넣어주기
    db.insta_review.insert_one(review_data)

    return jsonify({'result':'success','msg':"POST 리뷰가 성공적으로 저장"})


@app.route('/review', methods=['GET'])
def read_reviews():
    #mongodb에서 가져오기
    review_list = list(db.insta_review.find({},{'_id':0})) #_id빼고...
    #가져온 데이터 리스트 JSON으로 돌려주기
    return jsonify({'result': 'success', 'reviews': review_list}) #-> ajax에서는



@app.route('/test')
def posting():
    return render_template('test.html')


# flask를 실행 시켜주는 공간
if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)