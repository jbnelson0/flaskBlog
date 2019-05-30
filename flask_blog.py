from flask import Flask, render_template, url_for
from Forms import RegistrationForm, LoginForm
app = Flask(__name__)


app.config['SECRET_KEY'] = 'de104ecad906b0ca18ef455a25c32172'


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

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
