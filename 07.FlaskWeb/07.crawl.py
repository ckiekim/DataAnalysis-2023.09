from flask import Flask, render_template 
import util.crawl_util as cu

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h1>크롤링</h1>
        <button onclick="location.href='/interpark'">인터파크 베스트셀러</button>
        <button onclick="location.href='/melon'">멜론 실시간 차트 Top50</button>
        <button onclick="location.href='/siksin'">영등포역 맛집</button>
    '''

@app.route('/interpark')
def interpark():
    book_list = cu.get_bestseller()
    return render_template('07.interpark.html', book_list=book_list)

@app.route('/melon')
def melon():
    song_list = cu.get_melon_chart()
    return render_template('07.melon.html', song_list=song_list)

@app.route('/siksin')
def siksin():
    rest_list = cu.get_restaurant_list('영등포역')
    return render_template('07.siksin.html', rest_list=rest_list)

if __name__ == '__main__':
    app.run(debug=True)