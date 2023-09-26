from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')     # localhost:5000/ 을 서비스하기 위한 코드
def index():
    return '<h1>상속</h1>'

@app.route('/child1')
def child1():
    return render_template('09.child1.html')

@app.route('/child2')
def child2():
    return render_template('09.child2.html')

if __name__ == '__main__':
    app.run(debug=True)