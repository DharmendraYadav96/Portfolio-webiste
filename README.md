#### https://portfolio-webiste-kf65.onrender.com
# 🧠 Dharmendra Yadav – Portfolio Website

This is my personal portfolio website built with **Flask**, showcasing my skills, blog posts, and data science projects. It also includes an interactive **YouTube AI Chatbot** that summarizes videos and answers questions using OpenAI and LangChain.

---

## 🚀 Features

- 🧑 About Me page with skills, experience, education, and contact info
- 📊 Projects page with deployed data science models
- ✍️ Blogs page rendered dynamically using JSON + Jinja
- 🤖 AI-powered YouTube Chatbot:
  - Accepts YouTube URL
  - Fetches transcript
  - Generates summary


---

## 📁 Project Structure



To run the file on local system, activate environment. Ten run code:
Run python app.py 
````
/portfolio-website
├── app.py # Main Flask app
├── requirements.txt # Dependencies
├── render.yaml # Render deployment config
│
├── /templates # Jinja HTML files
│ ├── base.html
│ ├── header.html
│ ├── footer.html
│ ├── home.html
│ ├── about.html
│ ├── blogs.html
│ ├── projects.html
│ └── youtube_chatbot.html
│
├── /static # CSS, JS, images
│ └── /images
│
├── /youtube_chatbot
  ├── routes.py # YouTube chatbot routes
  ├── utils.py # Transcript, summary, QA functions
  └── init.py


````

#### Set up virtual environment
````
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
````
#### Install dependencies
````
pip install -r requirements.txt
````
#### Set your OpenAI API key
````
OPENAI_API_KEY=your-openai-key
````
#### Run the app
````
flask run
````

## 🧠 Tech Stack
- Backend: Python, Flask
- Frontend: HTML, CSS, Bootstrap, Jinja2
- AI & NLP: OpenAI (GPT-3.5/4), LangChain
- YouTube Transcript: youtube-transcript-api
- Deployment: Render
