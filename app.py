from flask import Flask, render_template

from data.projects import projects
from data.experience import experience
from data.skills import skills
from data.blogs import blogs as blog_data

app = Flask(__name__)

# ---------------------------------
# Home
# ---------------------------------

@app.route("/")
def home():

    return render_template(
        "pages/home.html",
        projects=projects,
        experience=experience,
        skills=skills,
        blogs=blog_data,
        active_page="home"
    )


# ---------------------------------
# Blogs Page
# ---------------------------------

@app.route("/blogs")
def blogs():

    return render_template(
        "pages/blogs.html",
        blogs=blog_data,
        active_page="blogs"
    )


# ---------------------------------
# Contact
# ---------------------------------

@app.route("/contact")
def contact():

    return render_template(
        "pages/contact.html",
        active_page="contact"
    )


# ---------------------------------
# Chat
# ---------------------------------

@app.route("/chat")
def chat():

    return render_template(
        "pages/chat.html",
        active_page="chat"
    )


if __name__ == "__main__":
    app.run(debug=True)