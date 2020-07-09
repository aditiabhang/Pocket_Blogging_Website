from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '4f1d3c4fc5e98ee5c74d14e5402c95c5'

posts = [
    {
        'author': 'Aditi Abhang',
        'title': 'My first pocket thought',
        'content': "This is my first pocket blog content.",
        'date_posted': 'July 8, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'My second pocket thought',
        'content': "This is my second pocket blog content.",
        'date_posted': 'July 7, 2020'
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
    form = LoginForm
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
