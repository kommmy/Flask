#coding=utf-8
from flask.ext.wtf import Form, TextField, BooleanField,PasswordField,FileField,FieldList
from flask.ext.wtf import Required
from flask.ext.wtf import file_required
from wtforms import validators
from app.models import User
# class LoginForm(Form):
#     openid = TextField('openid', validators = [Required()])
#     remember_me = BooleanField('remember_me', default = False)
#     password = PasswordField('password',validators = [Required()])


class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.Required()])

class LoginForm(Form):
    username = TextField('Username', [validators.Required()])
    password = PasswordField('Password', [validators.Required()])
    remember_me = BooleanField('remember_me', default = False)
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        user = User.query.filter_by(
            username=self.username.data).first()
        if user is None:
            self.username.errors.append('Unknown username')
            return False

        if not user.password == self.password.data:
            self.password.errors.append('Invalid password')
            return False

        self.user = user
        return True

#测试上传
class FileList(Form):
    filelist = FieldList(TextField('Name', [validators.required()]))

class UploadForm(Form):
    upload = FileField("Upload your image",
                       validators=[file_required()])

