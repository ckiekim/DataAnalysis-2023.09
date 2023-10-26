import requests, json, os

def get_legal_answer(static_folder, question):
    openApiURL = "http://aiopen.etri.re.kr:8000/LegalQA"
    filename = os.path.join(static_folder, 'keys/etriAiKey.txt')
    with open(filename) as f:
        accessKey = f.read()
    headers = {"Content-Type": "application/json; charset=UTF-8", "Authorization": accessKey}
    requestJson = { "argument": { "question": question } }
    result = requests.post(openApiURL, headers=headers, data=json.dumps(requestJson)).json()
    if len(result['return_object']['LegalInfo']['AnswerInfo']) == 0:
        return {'result': 0, 'answer': '죄송합니다. 답을 찾지 못했습니다.'}
    else:
        res_dict = result['return_object']['LegalInfo']['AnswerInfo'][0]
        res_dict['result'] = 1
        return res_dict
