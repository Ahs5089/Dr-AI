from flask import Flask, render_template, request, jsonify
import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import load_model

# Download NLTK data
nltk.download('punkt')
nltk.download('wordnet')

app = Flask(__name__)
app.static_folder = 'static'

# Initialize components
lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')

# Crisis detection keywords
CRISIS_KEYWORDS = {'suicide', 'kill myself', 'end it all', 'self harm', 'emergency', 'want to die'}

def contains_crisis(text):
    text = text.lower()
    return any(keyword in text for keyword in CRISIS_KEYWORDS)

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    return [lemmatizer.lemmatize(word.lower()) for word in sentence_words]

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return [{'intent': classes[r[0]], 'probability': str(r[1])} for r in results]

def get_response(intents_list):
    try:
        tag = intents_list[0]['intent']
        for intent in intents['intents']:
            if intent['tag'] == tag:
                return random.choice(intent['responses'])
        return "I'm not sure how to respond to that. Could you rephrase?"
    except:
        return "I'm having trouble understanding. Please try again."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat_bot.html')

@app.route('/get')
def get_bot_response():
    user_text = request.args.get('msg')
    if contains_crisis(user_text):
        return jsonify({
            'response': "🚨 Please contact 988 immediately. You're not alone.",
            'emergency': True
        })
    ints = predict_class(user_text)
    response = get_response(ints)
    return jsonify({'response': response})

@app.route('/escalate')
def escalate_to_doctor():
    return jsonify({
        'response': "I'm connecting you to a licensed professional. One moment please...",
        'buttons': [
            {'text': 'Video Call', 'url': 'https://calendly.com/your-clinic/video-consult'},
            {'text': 'Text Chat', 'url': 'https://your-website.com/chat-with-doctor'}
        ]
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)