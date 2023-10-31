import requests, json, os, io
from PIL import ImageFont, ImageDraw, Image
from google.cloud import vision
import matplotlib.pyplot as plt

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

def proc_ocr(static_folder, filename, color, showText, size):
    key_file = os.path.join(static_folder, f'keys/ocr-project-403207-71dec4109944.json')
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_file
    client_options = {'api_endpoint': 'eu-vision.googleapis.com'}
    client = vision.ImageAnnotatorClient(client_options=client_options)

    with io.open(filename, 'rb') as img_file:
        content = img_file.read()
    image = vision.Image(content=content)
 
    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    img = Image.open(filename)
    draw = ImageDraw.Draw(img)
    color = (255,0,0) if color == 'red' else \
                (0,255,0) if color == 'green' else (0,0,255)
    size = int(size)
    for i in range(1, len(texts)):
        text = texts[i]
        x1 = text.bounding_poly.vertices[0].x
        y1 = text.bounding_poly.vertices[0].y
        x2 = text.bounding_poly.vertices[1].x
        y2 = text.bounding_poly.vertices[2].y
        draw.rectangle(((x1,y1), (x2,y2)), outline=color, width=2)
        if showText == 'yes':
            draw.text((x1+10, y1-20), text.description, 
                      font=ImageFont.truetype('malgun.ttf',size), fill=color)
    
    savefile = os.path.join(static_folder, 'result/ocr-result.png')
    plt.imshow(img)
    plt.axis('off')
    plt.savefig(savefile, format='png')
    mtime = os.stat(savefile).st_mtime

    return texts[0].description, int(mtime)