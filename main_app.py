from flask import Flask, render_template, request
from main import get_theme

app = Flask(__name__)

@app.route('/')
def hello():
    if request.args:
        text = request.args['text']
        theme = get_theme(text)
        return render_template('index.html', result=theme)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)