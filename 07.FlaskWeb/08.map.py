from flask import Flask, render_template, request
import util.map_util as mu

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h1>지도 시각화</h1>
        <button onclick="location.href='/station'">지하철역 찾기</button>

    '''

@app.route('/station', methods=['GET','POST'])
def station():
    if request.method == 'GET':
        return render_template('08.station_form.html')
    else:
        stations = request.form.getlist('station')
        mu.get_station_map(app.root_path, stations)     # static/img/station_map.html 파일
        return render_template('08.station_res.html')

if __name__ == '__main__':
    app.run(debug=True)