from flask import Flask, render_template, request, flash
from bp.crawling import crawl_bp
from bp.map import map_bp

app = Flask(__name__)
app.secret_key = 'qwert12345'       # flash와 session을 사용하려면 반드시 설정해야 함

app.register_blueprint(crawl_bp, url_prefix='/crawling')    # localhost:5000/crawling/* 는 crawl bp가 처리
app.register_blueprint(map_bp, url_prefix='/map')

@app.route('/')
def home():
    menu = {'ho':1, 'us':0, 'cr':0, 'ma':0, 'sc':0}
    flash('Welcome to my Web!!!')
    return render_template('home.html', menu=menu)

@app.route('/schedule')
def schedule():
    menu = {'ho':0, 'us':0, 'cr':0, 'ma':0, 'sc':1}
    return render_template('schedule.html', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)