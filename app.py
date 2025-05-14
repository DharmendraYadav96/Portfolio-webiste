from flask import Flask, render_template, abort, request, jsonify
import json
import os
# from chatbot.chatbot import GenAIChatbot

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", active_page = 'home')  # Or a proper home.html later

@app.route("/blogs")
def blogs():
    with open('blogs.json') as f:
        posts = json.load(f)
    return render_template("blog.html", posts=posts, active_page="blogs")

@app.route("/contacts")
def contacts():
    return render_template("contact.html", active_page = 'contacts')

@app.route('/chat')
def chat_page():
    return render_template('chat.html', active_page = 'Chatbot')

@app.route("/blogs/<slug>")
def blog_post(slug):
    template_path = f"blogs/{slug}.html"
    full_path = os.path.join(app.template_folder, template_path)
    if os.path.exists(full_path):
        return render_template(template_path)
    else:
        abort(404)



# @app.route('/ask', methods=['POST'])
# def ask():
#     user_message = request.json.get('message')
#     bot_response = chatbot.get_response(user_message)
#     return jsonify({'response': bot_response})

if __name__ == "__main__":
    app.run(debug=True)
