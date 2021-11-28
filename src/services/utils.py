from ..db.documents import Password

from cryptography.fernet import Fernet
from datetime import datetime
from decouple import config
import base64
import jwt


def base64_to_file(img_encoded):
    img = base64.b64decode(img_encoded)
    filename = str(datetime.now()).split('.')[-1] + '.jpg'

    with open('static/' + filename, 'wb') as file:
        file.write(img)
    
    return filename

def generate_token():
    payload = { 
        "generated_at": str(datetime.utcnow()),
        "Zeni": "Studios"
    }
    return jwt.encode(payload, config('JWT_SECRET'), algorithm="HS256")

def encrypt_password(password):
    f = Fernet(config('FERNET_KEY'))

    return f.encrypt(password.encode('ascii')).decode('utf-8')

def decrypt_password(password):
    f = Fernet(config('FERNET_KEY'))

    return f.decrypt(password.encode('ascii')).decode('utf-8')

def verify_password(password):
    session = Password.objects().first()
    current_password = decrypt_password(session.password)

    return current_password == password, session

def send_email():
    print('11111')
    import smtplib
    from email.message import EmailMessage
    print('22222')

    msg = EmailMessage()
    msg['Subject'] = 'New Contact Info'
    msg['From'] = 'info@maere.com.ec'
    msg['To'] = 'paola@maere.com.ec'
    msg.set_content('Mensaaaje')
    print('3333')

    with smtplib.SMTP_SSL('mail.maere.com.ec', 465) as smtp:
        try:
            print('4444')
            smtp.login('info@maere.com.ec', '')
            print('5555')
            smtp.send_message(msg)
            print('6666')
        except Exception as e:
            # print(e)
            print('❌❌❌')
            return False

    return True

