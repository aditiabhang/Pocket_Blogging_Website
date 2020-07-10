from flask import render_template, url_for, flash, redirect
from pocket_blog import app, db, bcrypt
from pocket_blog.forms import RegistrationForm, LoginForm
from pocket_blog.models import User, Post

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
    },
{
        'author': 'Kuku Sanket',
        'title': 'My favorite pocket thought',
        'content': "This is my favorite bestest best pocket blog content.",
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


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@pocket.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)
