from flask import Flask, render_template, url_for, flash, redirect 
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
def home():
    return  render_template('home.html', posts_data=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='Hey About')    

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form =LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@ga.com' and form.password.data == '123':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Unsuccessful login try again please "With a correct one NOW" ', 'danger')    
    return render_template('login.html',title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)