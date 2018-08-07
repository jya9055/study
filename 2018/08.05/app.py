from flask import Flask
from flask import render_template
from jya_gAPIclass import GapiClass

app = Flask(__name__)

@app.route('/mail')
def mail():
	return render_template('mailcontents.html')

@app.route('/send')
def send():
    instance = GapiClass()
	instance.sendMail(mail_title , mail_text, email, name)

if __name__ == '__main__':
	app.run()