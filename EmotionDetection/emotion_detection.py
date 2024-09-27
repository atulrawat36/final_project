import requests
import json
 
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}
   
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)
 
    # Access the first item in the emotionPredictions list
    emotion_predictions = formatted_response['emotionPredictions']
   
    if emotion_predictions:
        first_prediction = emotion_predictions[0]['emotion']
       
        # Extract scores
        anger_score = first_prediction['anger']
        disgust_score = first_prediction['disgust']
        fear_score = first_prediction['fear']
        joy_score = first_prediction['joy']
        sadness_score = first_prediction['sadness']
 
        # Determine the dominant emotion
        dominant_emotion = max(first_prediction, key=first_prediction.get)
 
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    else:
        return {
            'error': 'No emotion predictions available.'
        }


