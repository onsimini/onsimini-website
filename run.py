from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Gontran Sion',
        'title': 'Blog Post 1.',
        'content': 'First post content.',
        'date': 'October 10, 2021'
    },
    {
        'author': 'Gontran Sion',
        'title': 'Blog Post 2.',
        'content': 'Second post content.',
        'date': 'October 11, 2021'
    },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='about')

if __name__ == '__main__':
    app.run()
