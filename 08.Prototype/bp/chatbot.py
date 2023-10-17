from flask import Blueprint, render_template, request, current_app

chatbot_bp = Blueprint('chatbot_bp', __name__)

menu = {'ho':0, 'us':0, 'cr':0, 'ma':0, 'cb':1, 'sc':0}

@chatbot_bp.route('/counsel', methods=['GET','POST'])
def counsel():
    if request.method == 'GET':
        return render_template('chatbot/counsel.html', menu=menu)
    else:
        pass

@chatbot_bp.route('/bard', methods=['GET','POST'])
def bard():
    pass

@chatbot_bp.route('/genImg', methods=['GET','POST'])
def gen_img():
    pass