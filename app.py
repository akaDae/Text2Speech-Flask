from flask import Flask, render_template, request, send_file
from gtts import gTTS
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    mytext = request.form["text"]

    selected_language = request.form.get("language", "en")

    if selected_language == "el":
        language = "el"
    else:
        language = "en"
    myobj = gTTS(text=mytext, lang=language, slow=True)
    mp3_filename = "hxos.mp3"
    myobj.save(mp3_filename)
    return send_file(mp3_filename, as_attachment=True)


if __name__ == "__main__":
    app.run()
