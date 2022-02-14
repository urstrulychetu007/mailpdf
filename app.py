from flask import *
from flask_mail import Mail, Message
import urllib.request
app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'kletechseed_data@kletech.ac.in'
app.config['MAIL_PASSWORD'] = 'kletechseed_data'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)




@app.route('/<url>/<email>')
def index(url,email):
     msg = Message(
                'Hello',
                sender ='kletechseed_data@kletech.ac.in',
                recipients = [email]
               )
     msg.body = 'Hello Flask message sent from Flask-Mail'
     response = urllib.request.urlopen("http://10.2.0.23/uploads/Consents/"+url+".pdf")
     
     msg.attach(url+".pdf", "application/pdf", response.read()) 
     mail.send(msg)
     return render_template('index.html')


if __name__ == '__main__':
    app.run()