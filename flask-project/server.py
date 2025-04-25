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
        "Authorization": f"Bearer {api_key}",
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


@app.errorhandler(404)
def not_found(e):
    return render_template("error.html", error="Page not found (404)")

@app.errorhandler(500)
def server_error(e):
    return render_template("error.html", error="Internal server error (500)")

if __name__ == "__main__":
    app.run(debug=True)