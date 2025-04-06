from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return """
        For the given statement, the system response is 
            'anger': {},
            'disgust': {},
            'fear': {},
            'joy': {}
            and 
            'sadness': {}.
            The dominant emotion is {}
    """.format(anger, disgust, fear, joy, sadness, dominant_emotion)


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5500)

