from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']='6ca0f4e0b99dcd7bb9ab'

posts =[
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
     {
        'author': 'Solomon Drar',
        'title': 'Kiya 18 dekayk',
        'content': 'Heros kiya',
        'date_posted': 'July 07, 2001'
    },
    {
        'author': 'Kibreab Fre',
        'title': 'Babilon',
        'content': 'Enemy Tricks',
        'date_posted': 'May 18, 2003'
    }

]

@app.route("/")
@app.route("/home")
def hello():
    return  render_template('home.html', posts_data=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='Hey About')    

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form =LoginForm()
    return render_template('login.html',title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)