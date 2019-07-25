import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)
latinizer_url = 'https://hidden-journey-62459.herokuapp.com/piglatinize/'

def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


@app.route('/')
def home():
    print("DEBUG: Running get_fact()")
    post_data = get_fact()

    session = requests.Session()
    params = {'input_text': post_data.encode('utf-8')}
    response = session.post(latinizer_url, data=params)
    return response.content


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

