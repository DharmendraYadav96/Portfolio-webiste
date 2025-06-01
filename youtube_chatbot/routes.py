from flask import Blueprint, render_template, request
from youtube_chatbot.utils import extract_video_id, get_transcript, summarize_transcript

youtube_bp = Blueprint("youtube", __name__, template_folder="../templates")

@youtube_bp.route("/youtube-chatbot", methods=["GET", "POST"])
def youtube_chatbot_page():
    summary = None
    error = None
    if request.method == "POST":
        url = request.form.get("url")
        try:
            video_id = extract_video_id(url)
            transcript = get_transcript(video_id)
            summary = summarize_transcript(transcript)
        except Exception as e:
            error = f"Failed to process video: {str(e)}"
    return render_template("youtube_chat.html", summary=summary, error=error, active_page = 'Chatbot')
