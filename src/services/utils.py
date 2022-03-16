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

def send_email(contact):
    import smtplib
    from email.message import EmailMessage

    msg = EmailMessage()
    msg['Subject'] = 'NUEVO MENSAJE DE ' + contact.get('name') + ' en MAERE'
    msg['From'] = 'info@maere.com.ec'
    msg['To'] = 'paola@maere.com.ec,info@maere.com.ec'

    message = '''
        {name} ha enviado un mensaje a través de la página web de MAERE.

        Nombre: {name}
        Email: {email}
        Teléfono: {phone}
        Mensaje: {message}

        También lo puedes revisar en https://maere.com.ec/admin
    '''.format(**contact)
    msg.set_content(message)

    with smtplib.SMTP_SSL('mail.maere.com.ec', 465) as smtp:
        try:
            smtp.login('paola@maere.com.ec', 'crispaoli')
            smtp.send_message(msg)
        except Exception as e:
            pass
