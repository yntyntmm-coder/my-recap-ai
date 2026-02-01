
import os
import google.generativeai as genai
from flask import Flask, request, jsonify

# ၁။ မင်းရဲ့ API Key ကို ဒီမှာ အစားထိုးပါ
genai.configure(api_key="AIzaSyD1xHtTmNv4z0oiMhUBqAw8U3H1mstycos")

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is Live!"

@app.route('/recap', methods=['POST'])
def do_recap():
    try:
        data = request.get_json()
        video_url = data.get('url')
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(f"Please summarize this video in Burmese: {video_url}")
        return response.text
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
