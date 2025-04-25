# save this as app.py
from flask import Flask, render_template, redirect, session,request
import requests

app = Flask(__name__)
app.secret_key = "secure key"


@app.route("/", methods = ['GET'])
def index():
    return render_template('index.html')

@app.route("/gen_image", methods = ['POST'])
def gen_img():
    cmd_prompt_txt = request.form['command-prompt-txt']
    api_key = '05a631026aba427880be35523ae83a46'
    response = requests.post("https://api.aimlapi.com/v1/images/generations",
    headers={
        "Authorization": "Bearer "+api_key,
        "Content-Type": "application/json"
    },
    json={  # Use 'json' instead of 'data' for proper JSON handling
        "model": "dall-e-3",
        "prompt": cmd_prompt_txt,
        "n": 1,
        "quality": "standard",
        "response_format": "url",
        "size": "1024x1024",
        "style": "vivid"
    }
    )
    data = response.json()
    image_url = data['data'][0]['url'] if data.get('data') else None
    print(image_url)

    return render_template('index.html', image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)