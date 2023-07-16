from collections import defaultdict
import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)

port = 8001

@app.route('/getData/<key>', methods=["GET"])
def scrapeData(key):

    print("Using Port :", port)
    url_sDeal1 = 'https://www.snapdeal.com/search?keyword=' + key   
    source_code = requests.get(url_sDeal1)
    plain_text = source_code.text
    
    soup = BeautifulSoup(plain_text, "html.parser")
    resJson, resJsonObj = [], dict()
    for html in soup.find_all('div', {'class': 'favDp'}):
        for heading in html.find_all('p', {'class': 'product-title'}):
            resJsonObj["name"] = heading.text
        for p in html.find_all('span', {'class': 'product-price'}):
            resJsonObj["price"] = p.text
        for l in html.find_all('a', {'class': 'dp-widget-link'}):
            resJsonObj["link"] = l.get('href')
        resJson.append(resJsonObj.copy())
    return jsonify({"products": resJson})

@app.route("/", methods = ["GET"])
def index():
    print("Root Index")
    return "Hello World"

if __name__ == "__main__":
    app.run("127.0.0.1", port)


#.\venv\Scripts\activate 