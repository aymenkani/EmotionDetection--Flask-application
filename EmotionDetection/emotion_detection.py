import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    jsonobj = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=jsonobj, headers=headers)

    # If Watson API rejects input with 400
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    response_obj = json.loads(response.text)
    emotion = response_obj["emotionPredictions"][0]["emotion"]

    anger_score = emotion["anger"]
    disgust_score = emotion["disgust"]
    fear_score = emotion["fear"]
    joy_score = emotion["joy"]
    sadness_score = emotion["sadness"]

    dominant_emotion = max(emotion, key=emotion.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
