from flask import Flask, request, jsonify  #flask frameworkünü kullandığım için ekledim ve javascrpipt objeck notation olarak belirttim

app = Flask(__name__)

@app.route('/', methods=['GET'])   # https://www.geeksforgeeks.org/flask-app-routing/ bu kısımdan yararlandım
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
    app.run(debug=True)






























