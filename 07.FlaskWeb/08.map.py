from flask import Flask, render_template, request
import util.map_util as mu

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h1>지도 시각화</h1>
        <button onclick="location.href='/station'">지하철역 찾기</button>
        <button onclick="location.href='/cctv'">구별 CCTV/인구 현황</button>
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
    mu.get_cctv_pop(app.static_folder)      # static/img/cctv.html 파일
    return render_template('08.cctv.html')

if __name__ == '__main__':
    app.run(debug=True)