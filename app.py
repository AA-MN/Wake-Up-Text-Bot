from flask import Flask, render_template, request
import json
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



@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        waketime = request.form.get("waketime")
        reason = request.form.get("reason")
        quote = request.form.get("quote")
        ntfy_topic = request.form.get("ntfy_topic")
        print(waketime, reason, quote, ntfy_topic)
        return render_template("home.html", posts=posts)
    else:
        return render_template("home.html", posts=posts)

settings = {
    "waketime": waketime,
    "reason": reason,
    "quote": quote,
    "ntfy_topic": ntfy_topic
}

with open(settings.json, "w") as f:
    json.dump(settings, f)




@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)
