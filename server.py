"""
This module provides a Flask-based server for the Emotion Detection application.
The server handles requests to analyze text and returns the detected emotions.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    This function initiates the sentiment analysis for the text string
    provided as an argument by the user via the interface.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # Here is where we "catch" the numbers (scores)
    ang = response['anger']
    dis = response['disgust']
    fea = response['fear']
    joy = response['joy']
    sad = response['sadness']
    dom = response['dominant_emotion']

    # Check if the dominant emotion is None, indicating an error or invalid input
    if dom is None:
        return "Invalid text! Please try again!."
    return (f"For the given statement, the system response is "
            f"'anger': {ang}, 'disgust': {dis}, 'fear': {fea}, "
            f"'joy': {joy} and 'sadness': {sad}. "
            f"The dominant emotion is {dom}.")


@app.route("/")
def render_index_page():
    """
    This function initiates the rendering of the main application
    page over the Flask dev server.
    """
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
