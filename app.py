from flask import Flask, render_template
app = Flask(__name__)

posts = [

    {
        'author': 'Anand',
        'title': 'Wake Up Text Bot',
        'content': 'This is a wake up text bot that sends a text to yourself to wake up in the morning',
        'date_posted': 'November 06, 2026'
    },

    {
        'author': 'Anand',
        'title': 'Wake Up Text Bot',
        'content': 'This is a wake up text bot that sends a text to yourself to wake up in the morning',
        'date_posted': 'November 06, 2026'
    }
]

@app.route("/home")
def hello():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)
