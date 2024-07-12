from flask import Flask, jsonify
import json 

app = Flask(__name__)

# Örnek ürün verileri (products.json'dan alınacak)
products = []

@app.route('/', methods=['GET'])
def get_products():
    # products.json dosyasından verileri oku
    with open('products.json', 'r', encoding='utf-8') as f:
        products = json.load(f)
    return jsonify(products)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

