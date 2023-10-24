from flask import Blueprint, render_template, request, current_app
import util.map_util as mu
import os, json

map_bp = Blueprint('map_bp', __name__)

menu = {'ho':0, 'us':0, 'cr':0, 'ma':1, 'cb':0, 'sc':0}

@map_bp.route('/station', methods=['GET','POST'])
def station():
    if request.method == 'GET':
        return render_template('map/station_form.html', menu=menu)
    else:
        stations = request.form.getlist('station')
        stations = [station for station in stations if len(station.strip()) != 0]
        mu.get_station_map(current_app.root_path, stations)     # static/img/station_map.html 파일
        return render_template('map/station_res.html', menu=menu)

@map_bp.route('/cctv_pop', methods=['GET','POST'])
def cctv_pop():
    if request.method == 'GET':
        columns = ['CCTV댓수','최근증가율','인구수','내국인','외국인','고령자','외국인 비율','고령자 비율']
        colormaps = ['RdPu', 'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds', 'YlOrBr', 'YlOrRd', 
                     'OrRd', 'PuRd', 'BuPu', 'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']
        return render_template('map/cctv_pop_form.html', columns=columns, colormaps=colormaps, menu=menu)
    else:
        column = request.form['column']
        colormap = request.form['colormap']
        mu.get_cctv_pop(current_app.static_folder, column, colormap)    # static/img/cctv_pop.html 파일
        return render_template('map/cctv_pop_res.html', column=column, colormap=colormap, menu=menu)
    
@map_bp.route('/kakaoMap', methods=['GET','POST'])
def kakao_map():
    if request.method == 'GET':
        with open(os.path.join(current_app.static_folder, 'keys/카카오맵jsApiKey.txt')) as f:
            kakao_map_api_key = f.read()
        return render_template('map/kakao_map.html', menu=menu, key=kakao_map_api_key)
    else:
        level = request.form['level']
        lat = request.form['lat']
        lng = request.form['lng']
        return json.dumps([level, lat, lng])

@map_bp.route('/kakaoMapAdvanced', methods=['GET','POST'])
def kakao_map_advanced():
    if request.method == 'GET':
        with open(os.path.join(current_app.static_folder, 'keys/카카오맵jsApiKey.txt')) as f:
            kakao_map_api_key = f.read()
        return render_template('map/kakao_map_advanced.html', menu=menu, key=kakao_map_api_key)
    else:
        kind = request.form['kind']
        name = request.form['name']
        lat = request.form['lat']
        lng = request.form['lng']
        print(kind, name, lat, lng)
        return json.dumps([kind, name, lat, lng])