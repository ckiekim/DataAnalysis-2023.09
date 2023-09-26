from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')     # localhost:5000/ 을 서비스하기 위한 코드
def index():
    return '<h1>부트스트랩</h1>'

@app.route('/list')
def list():
    return render_template('10.list.html')



if __name__ == '__main__':
    app.run(debug=True)