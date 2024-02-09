import requests
import json


def emotion_detector(text_to_analyze):
   url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
   headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
   myobj = { "raw_document": { "text": text_to_analyze } }
   response = requests.post(url, json = myobj, headers=headers)
   formatted_response = json.loads(response.text)
   anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
   disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
   fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
   joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
   sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
   dominant_emotion = max(zip(formatted_response['emotionPredictions'][0]['emotion'].values(), formatted_response['emotionPredictions'][0]['emotion'].keys()))[1]
   return {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness, 'dominant_emotion': dominant_emotion}
