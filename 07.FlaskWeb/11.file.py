import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>파일 업로드</h2>'

@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'GET':
        return render_template('11.file_form.html')
    else:
        file_image = request.files['image']
        fname = file_image.filename             # 업로드한 파일 이름
        filename = os.path.join(app.static_folder, f'upload/{fname}')
        file_image.save(filename)
        return render_template('11.file_res.html', fname=f'upload/{fname}')

if __name__ == '__main__':
    app.run(debug=True)