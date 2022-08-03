import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.hs6yqo9.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

import requests
from bs4 import BeautifulSoup


@app.route('/')
def main():
    key = 'AD76BB131FF7E99097AB027CF51EBA025507AA02532786510CF4FC402A45D0FD'
    url = 'http://book.interpark.com/api/bestSeller.api?key=' + key + '&categoryId=100&output=json'
    r = requests.get(url)
    response = r.json()  # 결과를 json형태로 바꿔 response에 담아준다.
    rows = response['item']

    return render_template("index.html", rows=rows)


@app.route('/detail/<keyword>')
def detail(keyword):
    url = f"http://book.interpark.com/api/search.api?key=AD76BB131FF7E99097AB027CF51EBA025507AA02532786510CF4FC402A45D0FD&query={keyword}&start=1&maxResults=1&output=json"

    r = requests.get(url)
    response = r.json()  # 결과를 json형태로 바꿔 response에 담아준다.
    # insert

    return render_template("detail.html", response=response,title=keyword)  # parameter를 넣어서 보내준다.
    # 앞의 변수이름 render parameter이름은 같아도 되고 달라도 된다.


# @app.route('/detail/review', methods=["POST"])
# def save_review():
#     star_receive = request.form['star_give']
#     review_receive = request.form['review_give']
#     title_receive = request.form['title_give']
#
#     doc = {
#             'review': review_receive,
#             'star': star_receive,
#             'title':title_receive
#         }
#     db.review.insert_one(doc)
#
#
#     return jsonify({'msg': 'POST 연결 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
