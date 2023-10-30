from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page"

@app.route('/hello')
def hello():
    name = request.args.get('name', 'Guest')
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)