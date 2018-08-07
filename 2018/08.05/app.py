from flask import Flask
from flask import render_template
from jya_gAPIclass import GapiClass

app = Flask(__name__)

@app.route('/mail')
def mail():
	return render_template('mailcontents.html')

# 1. /mail 페이지에서 정보(1, 2)를 입력 받아, [발송] 버튼을 누르면 /send로 이동

@app.route('/send')
def send():
    instance = GapiClass()
	instance.sendMail(mail_title , mail_text, email, name)

# 2. 입력된 정보(1)를 바탕으로 pystache를 이용하여 메일 콘텐츠를 만들어주고
# 3. 입력된 정보(2)를 함수(sendMail)에 들어가는 변수로 넣어줌
# 4. 앞의 과정이 완료되면 실제 메일 발송하고 완료 메시지를 띄움 ('발송되었습니다')

# 입력된 정보를 활용하는 법을 모르겠어요!!

if __name__ == '__main__':
	app.run()