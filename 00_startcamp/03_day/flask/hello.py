from flask import Flask
app = Flask(__name__)

@app.route('/')#따옴표는 싱글로!#이거 하나가 서버 하나인 것
def hello():
    return 'ssafy!'

@app.route('/ssafy')
def hello2():
    return 'This is ssafy!'