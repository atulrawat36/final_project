from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=["GET"])
def emot_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    if 'error' in response:
        return response['error']  # Return the error message if no predictions are available

    # Extract scores and dominant emotion from the response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Return a formatted string with the scores and the dominant emotion
    return (
        f"For the given statement, the scores are: "
        f"Anger: {anger_score}, Disgust: {disgust_score}, Fear: {fear_score}, "
        f"Joy: {joy_score}, Sadness: {sadness_score}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/", methods=["GET"])
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1500)
