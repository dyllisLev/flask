# -*- coding: utf-8 -*-
# 인코딩선언

from flask import Flask
app = Flask(__name__)
#플라스크 모듈에 있는 플라스크 클래스르 임포트 한다
#플라스크 애플리케이션 모듈명을 Flask 클래스의 첫번째 인자로 넘겨주며 클라스크 애플리케이션 객체인 app을 생성한다
#이 플라스크 객체로 모든 플라스크 기능을 사용 할 수 있다.

@app.route("/")
#특정 URL을 호출했을 때 호출되는 함수를 정의 한다.
def hello():
    return "Hello World!"
#루트경로를 호출시 hello() 함수를 호출한다.
#hello() 함수는 "hello() World!" 를 리턴한다.

if __name__ == "__main__":
    app.run()
#메인모듈이 실행되었으면 로컬서버 함수를 실행한다.
    
