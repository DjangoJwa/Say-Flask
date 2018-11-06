from flask import Flask, request
from flask_cors import CORS
# 웹에서는 CORS 처리 안해주면 크롬같은 애버그린 브라우저에서 문제가 나기 떄문에 CORS문제를 해결해주는 모듈!

app = Flask(__name__)
CORS(app)


@app.route('/')
# method를 지정안하면 get이 default임
def hello_world():
    return 'Hello World!'

@app.route('/test', methods=['GET', 'POST'])
# 한 라우트에 method를 여러개 설정이 가능함
# 또한 method에 따라 값을 다르게 하는 것도 가능
def post_test():
    if request.method == 'GET':
        return 'GET이구나~'
    elif request.method == 'POST':
        return 'POST이구나~'

app.add_url_rule('/2', 'something', lambda: 'Hi!')

if __name__ == '__main__':
    app.run(debug=True)
