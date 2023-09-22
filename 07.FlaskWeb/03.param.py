from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')     # localhost:5000/ 을 서비스하기 위한 코드
def index():
    return '<h1>파라메터 전달값 받기</h1>'

# localhost:5000/area?pi=3.14&radius=10
@app.route('/area')
def area():
    pi = request.args.get('pi', '3.14159')      # default 값을 지정할 수 있음
    radius = request.values['radius']           # GET/POST 모두 사용할 수 있음
    result = float(pi) * float(radius) ** 2
    return f'<h1>pi={pi}, radius={radius}, area={result}</h1>'

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('02.login.html')
    else:
        uid = request.form['uid']
        pwd = request.values['pwd']
        return f'<h1>uid={uid}, pwd={pwd} 환영합니다.</h1>'

@app.route('/sample', methods=['GET','POST'])
def sample():
    if request.method == 'GET':
        return render_template('02.sample.html')
    else:
        a = int(request.form['a'])
        b = int(request.form['b'])
        return f'<h1>a={a}, b={b}, a * b = {a*b}</h1>'

if __name__ == '__main__':
    app.run(debug=True)