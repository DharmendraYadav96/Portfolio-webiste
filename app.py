from flask import Flask, render_template, abort
import json
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")  # Or a proper home.html later

@app.route("/blogs")
def blogs():
    with open('blogs.json') as f:
        posts = json.load(f)
    return render_template("blog.html", posts=posts, active_page="blogs")

@app.route("/contacts")
def contacts():
    return render_template("contact.html", active_page = 'contacts')

@app.route("/blogs/<slug>")
def blog_post(slug):
    template_path = f"blogs/{slug}.html"
    full_path = os.path.join(app.template_folder, template_path)
    if os.path.exists(full_path):
        return render_template(template_path)
    else:
        abort(404)

if __name__ == "__main__":
    app.run(debug=True)
