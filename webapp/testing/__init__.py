from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/bump')
def bump():
	return render_template("template.html")
if __name__ == '__main__':
    app.run(host="192.168.0.22")
