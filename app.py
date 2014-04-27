import os
from flask import Flask

import requests
import urllib

app = Flask(__name__)

@app.route('/')
def index():
    urlEndPoint = 'http://thecatapi.com'
    imageGetPath = '/api/images/get'
    values = {'format':'html',
            'results_per_page':10}
    r = requests.get(urlEndPoint + imageGetPath + "?" +  urllib.urlencode(values))
    arr = r.text.split('\n')
    result = ""
    for tag in arr:
        result += "<div>" + tag + "</div>"
    result += ""
    return result

if __name__ == "__main__":
    app.run(port=8000)
