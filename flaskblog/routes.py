from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


posts = [
    {
        'author': 'James Nelson',
        'title': 'Blog Post 1',
        'content': 'Post information and content',
        'date_posted': 'April 20, 2019'
    },
    {
        'author': 'John Smith',
        'title': 'Blog Post 2',
        'content': 'Post information and content',
        'date_posted': 'April 23, 2019'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    #check form valid
    if form.validate_on_submit():
        #hash password
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        #insert user(data from reg form) into db
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account has been created! You can now log in!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        #check db to validate email
        user = User.query.filter_by(email=form.email.data).first()
        #check password in db/hash matches
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            #set user as logged in
            login_user(user, remember=form.remember.data)
            #next param from url (to go back to this page after login required error)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and Password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
