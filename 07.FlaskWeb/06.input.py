from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h1>입력값 받기</h1>
        <button onclick="location.href='/calc'">셀렉트(calc 사례)</button>
        <button onclick="location.href='/lang'">라디오 및 체크박스(lang, food 사례)</button>
    '''

@app.route('/calc', methods=['GET','POST'])
def calc():
    if request.method == 'GET':
        op_list = ['+', '-', '*', '/', '//', '%', '**']
        return render_template('06.calc_form.html', op_list=op_list)
    else:
        num1 = int(request.form['num1'])
        op = request.form['op']
        num2 = int(request.form['num2'])
        result = eval(f'{num1}{op}{num2}')
        return f'''
            <h2>{num1} {op} {num2} = {result}</h2>
            <button onclick="location.href='/calc'">재실행</button>
        '''

@app.route('/lang', methods=['GET','POST'])
def lang():
    lang_dict = {'en':'영어', 'fr':'프랑스어', 'es':'스페인어', 'jp':'일본어', 'cn':'중국어'}
    food_list = ['삼겹살', '갈비탕', '불고기', '피자', '햄버거']
    if request.method == 'GET':
        return render_template('06.lang_food.html', lang_dict=lang_dict, food_list=food_list)
    else:
        language = request.form['language']
        foods = request.form.getlist('food')
        selected_foods = []
        for food_index in foods:
            selected_foods.append(food_list[int(food_index)])

        return f'''
            <h2>선택한 언어: {lang_dict[language]}</h2>
            <h2>선택한 음식: {selected_foods}</h2>
            <button onclick="location.href='/lang'">재실행</button>
        '''

if __name__ == '__main__':
    app.run(debug=True)
