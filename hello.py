import os
from winning_predictor2 import predict
from flask import json
from flask import Flask
from flask import render_template
from flask import jsonify
app = Flask(__name__, static_url_path='/static')

with open(os.path.join(os.path.dirname(__file__),'data_ids.json'),'r', encoding='utf-8') as data_file:
    data = json.load(data_file)
    
def find_in_data(name):
    for x in data:
        if x['id'] == name:
            return x

@app.route('/')
def home():
    return render_template('index.html')
          
@app.route('/info/')
def info_empty():
    return jsonify(message="Error project not found")
@app.route('/info/<name>')
def info(name):
    message=find_in_data(name)
    return jsonify(message=json.dumps(message, indent=4, separators=(',', ': '))) 

@app.route('/predict/')
def predict_nil():
    return jsonify(win=False)

@app.route('/predict/<name>')
def predictt(name):
    return jsonify(win=str(predict(find_in_data(name))))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
    
