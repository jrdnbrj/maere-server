from datetime import datetime
import base64


def base64_to_file(img_encoded):
    img = base64.b64decode(img_encoded)
    filename = str(datetime.now()).replace(' ', '').replace(':', '_') + '.jpg'

    with open('static/' + filename, 'wb') as file:
        file.write(img)
    
    return filename
