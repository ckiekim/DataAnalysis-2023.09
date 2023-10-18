from flask import Blueprint, render_template, current_app
import util.crawl_util as cu

crawl_bp = Blueprint('crawl_bp', __name__)

menu = {'ho':0, 'us':0, 'cr':1, 'ma':0, 'cb':0, 'sc':0}

@crawl_bp.route('/melon')
def melon():
    print(current_app.root_path)    # bp module에서는 app 대신에 current_app을 사용
    song_list = cu.get_melon_chart()
    return render_template('crawling/melon.html', song_list=song_list, menu=menu)

@crawl_bp.route('/interpark')
def interpark():
    book_list = cu.get_bestseller()
    return render_template('crawling/interpark.html', book_list=book_list, menu=menu)