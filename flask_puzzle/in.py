from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    if request.args:
        name = request.args['text']
        return render_template('in.html', result='Hello, ' + name)

    return render_template('in.html')

if __name__ == '__main__':
    app.run(debug=True)