#flask frameworkünü kullandığım için ekledim ve javascrpipt object notation olarak belirttim
from flask import Flask, request, jsonify  

app = Flask(__name__)
# https://www.geeksforgeeks.org/flask-app-routing/ bu kısımdan yararlandım
@app.route('/', methods=['GET'])   
def home():
    return jsonify({"msg": "BC4M"})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"})

@app.route('/', methods=['POST'])
def post_data():
    data = request.get_json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)































