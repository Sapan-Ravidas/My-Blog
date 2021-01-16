from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title="Welcome", posts = posts) 


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/login")
def login():
    return render_template('login.html', title="Login")


@app.route("/signup")
def signup():
    return render_template('signup.html', title = "Sign-Up")


@app.route("/help")
def help():
    return render_template('help.html', title = "Help")


if __name__ == '__main__':
    app.run(debug=True)
