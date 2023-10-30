from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']
    return render_template('result.html', user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)