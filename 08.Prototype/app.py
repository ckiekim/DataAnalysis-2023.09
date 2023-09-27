from flask import Flask, render_template, request
import util.crawl_util as cu

app = Flask(__name__)

@app.route('/')
def home():
    menu = {'ho':1, 'us':0, 'cr':0, 'sc':0}
    return render_template('home.html', menu=menu)

@app.route('/melon')
def melon():
    menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
    song_list = cu.get_melon_chart()
    return render_template('melon.html', song_list=song_list, menu=menu)


@app.route('/schedule')
def schedule():
    menu = {'ho':0, 'us':0, 'cr':0, 'sc':1}
    return render_template('schedule.html', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)