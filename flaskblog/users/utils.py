import secrets
import os
from PIL import Image
from flask_mail import Message
from flask import url_for, current_app
from flaskblog import mail

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    # _ replaces any variable you want to throw away -- here it is f_name would replace the _ in next line
    _, f_ext = os.path.splitext(form.picture.filename)
    picture_fn = random_hex + f_ext
    #this updates the picture and file name uploaded for future saving/use
    picture_path = os.path.join(current_app.route_path, 'static/profile_pics', picture_fn)
    #resize image before saving and save file to db with file name/path created above
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='testing@demo.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request, simply ignore this email and no changes will be made
'''
    mail.send(msg)
