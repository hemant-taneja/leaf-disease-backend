from flask import Flask, request, jsonify
from PIL import Image
from flask_cors import CORS
from predict import predict_image
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
   return "Hello World!"

@app.route('/prediction', methods=["POST"])
def get_prediction():
    print(request.files['file'])
    file = request.files['file']
    im = Image.open(file).convert('RGB')
    res = predict_image(im)
    return {"prediction":str(res)}

if __name__ == "__main__":
    app.run()