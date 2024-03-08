"""
this is the starting file of the server
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    recieves the results of emotion detector and sends response
    """
    text_to_analyze = request.args.get('textToAnalyze')
    dominant_emotion = emotion_detector(text_to_analyze)
    dominant_emotion_score = dominant_emotion['dominant_emotion']

    if dominant_emotion_score is None:
        return "Invalid text! Please try again."
    return f"The given text has been identified as {dominant_emotion}."

@app.route("/")
def render_index_page():
    """
    goes to index
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
