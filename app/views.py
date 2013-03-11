#coding=utf-8
import os
from flask import session
from flask import render_template,flash,redirect, g
from flask import request, url_for
from flask.ext.login import current_user, logout_user, login_user, login_required, confirm_login
from werkzeug.utils import secure_filename
from app import app,db,loginmanager
from app.forms import LoginForm,RegistrationForm
from app.models import User

@loginmanager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print form.user.get_id()
        print form.user.username,form.user
        login_user(form.user,form.remember_me.data)
        flash(u'恭喜您登录成功 %s' % form.user.username)
        # g.name = form.user.username
        # session['user_id'] = form.user.id
        # return redirect(url_for('index',name = form.user.username))
        return redirect(request.args.get("next") or url_for("index"))
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(u'感谢您的注册')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/')
@app.route('/index/')
def index():
    print app.root_path
    print app.config
    if not current_user.is_authenticated():
        owner = u'游客'
    else:
        owner = current_user.username
        email = current_user.email
    users= [{'author':{'name':'nicky'},'body':'Hello World'},{'author':{'name':'andy'},'body':'Come On!'}]
    title = 'HOME PAGE'

    return render_template('hello.html',title = title,users = users,name = owner)



#上传
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/test', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        fileobj = request.files['file']
        if file and allowed_file(fileobj.filename):
            filename = secure_filename(fileobj.filename)
            fileobj.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template('upload.html')

@app.route('/uploads/')
def uploaded_file():
    # return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    return u'上传完成'

##测试上传
# @app.route("/upload/", methods=("GET", "POST"))
# def upload():
#     form = UploadForm()
#     if form.validate_on_submit():
#         print 1
#         filename = form.upload.data
#     else:
#         filename = None
#     print form.upload.name
#     print form.upload.file
#     return render_template("upload.html",
#                            form=form,
#                            filename=filename)