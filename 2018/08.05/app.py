from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/mail')
def mail():
	return render_template('mailcontents.html')

@app.route('/send')
def send():
    return

if __name__ == '__main__':
	app.run()