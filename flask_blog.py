from flask import Flask, render_template


app = Flask(__name__)


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

if __name__ == '__main__':
    app.run(debug=True)