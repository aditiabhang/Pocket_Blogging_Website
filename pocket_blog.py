from flask import Flask, render_template

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)
