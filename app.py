from flask import *
from flask_mail import Mail, Message
import urllib.request
app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'apsuser7@kletech.ac.in'
app.config['MAIL_PASSWORD'] = 'Apsuser7'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/')
def open():
     return render_template('index.html')

@app.route('/<url>/<email>')
def index(url,email):
     msg = Message(
                'Hello user',
                sender ='apsuser7@kletech.ac.in',
                recipients = [email]
               )
     msg.body = 'Your consent has been attached with this mail.'
     response = urllib.request.urlopen("http://210.212.192.31:8080/uploads/Consents/"+url+".pdf")
     
     msg.attach(url+".pdf", "application/pdf", response.read()) 
     mail.send(msg)
     return render_template('index.html')


if __name__ == '__main__':
    app.run()
