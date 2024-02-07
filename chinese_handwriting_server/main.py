from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from PIL import Image, ImageOps
from io import BytesIO
import base64

import torch
from model import Recognizer
from torchvision import transforms


device = torch.device('cpu')

model = Recognizer()
model.load_state_dict(torch.load('recognizer.pth', map_location=device))
model.eval()

vocabulary_list = ["起","果","热","院","四","回","西","国","高","怎","系","北","一","七","三","上","下","不","东","子","医","字","个","十","中","午","气","学","么","开","水","九","习","书","汉","雨","买","见","视","零","觉","了","二","在","五","些","生","坐","电","块","影","很","校","客","样","家","桌","去","京","亮","想","友","人","没","什","对","今","叫","他","们","面","候","苹","做","小","少","吃","同","名","后","吗","听","会","爱","爸","租","呢","住","岁","作","你","和","茶","椅","的","车","站","那","钟","哪","狗","认","识","话","日","都","语","时","菜","说","请","读","儿","先","钱","我","八","六","老","关","兴","这","再","写","打","商","猫","谁","明","星","昨","飞","谢","是","喂","多","喜","喝","大","天","冷","看","太","几","出","女","她","好","睡","妈","工","现","衣","能","里","分","饭","馆","姐","前","欢","师","脑","火","漂","月","有","朋","服","年","期","本","米","店","机","来","杯","点"]

app = Flask(__name__)
CORS(app)

@app.route('/trace', methods=['POST'])
def post_image():
     if request.method == 'POST':
        image = request.form['image'].split(',')[1]

        image = Image.open(BytesIO(base64.b64decode(image)))
        new_image = Image.new("RGBA", image.size, "WHITE")
        new_image.paste(image, (0, 0), image)
        image = new_image.convert('LA')
        image = transforms.Resize(64)(image)
        image = transforms.Grayscale(num_output_channels=1)(image)

        image.save('image.png', 'PNG')
        image = transforms.ToTensor()(image).unsqueeze_(0)

        with torch.no_grad():
            
            prediction = model(image)
            prediction = vocabulary_list[prediction[0].argmax(-1)]  

        return jsonify({'character': prediction})

if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host="0.0.0.0", port=5100)
