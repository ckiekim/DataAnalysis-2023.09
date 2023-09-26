from flask import Flask, render_template, request
import util.map_util as mu

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h1>지도 시각화</h1>
        <button onclick="location.href='/station'">지하철역 찾기</button>
        <button onclick="location.href='/cctv'">구별 CCTV댓수 현황</button>
        <button onclick="location.href='/cctv_pop'">구별 CCTV/인구 현황(개선판)</button>
    '''

@app.route('/station', methods=['GET','POST'])
def station():
    if request.method == 'GET':
        return render_template('08.station_form.html')
    else:
        stations = request.form.getlist('station')
        stations = [station for station in stations if len(station.strip()) != 0]
        mu.get_station_map(app.root_path, stations)     # static/img/station_map.html 파일
        return render_template('08.station_res.html')

@app.route('/cctv')
def cctv():
    mu.get_cctv(app.static_folder)      # static/img/cctv.html 파일
    return render_template('08.cctv.html')

@app.route('/cctv_pop', methods=['GET','POST'])
def cctv_pop():
    if request.method == 'GET':
        columns = ['CCTV댓수','최근증가율','인구수','내국인','외국인','고령자','외국인 비율','고령자 비율']
        colormaps = ['RdPu', 'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds', 'YlOrBr', 'YlOrRd', 
                     'OrRd', 'PuRd', 'BuPu', 'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']
        return render_template('08.cctv_pop_form.html', columns=columns, colormaps=colormaps)
    else:
        column = request.form['column']
        colormap = request.form['colormap']
        mu.get_cctv_pop(app.static_folder, column, colormap)    # static/img/cctv_pop.html 파일
        return render_template('08.cctv_pop_res.html', column=column, colormap=colormap)

if __name__ == '__main__':
    app.run(debug=True)