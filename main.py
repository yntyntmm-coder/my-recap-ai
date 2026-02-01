import os
import google.generativeai as genai
from flask import Flask, request

# --- မင်းရဲ့ API Key ကို အောက်က မျက်တောင်ဖွင့်ပိတ်ထဲမှာ ထည့်ပါ ---
API_KEY = "မင်းရဲ့_API_Key_ကို_ဒီမှာထည့်" 
# --------------------------------------------------

genai.configure(api_key=API_KEY)
app = Flask(__name__)

@app.route('/recap', methods=['POST'])
def do_recap():
    try:
        # App ဆီက ပို့လိုက်တဲ့ Data ကို လက်ခံခြင်း
        data = request.json
        video_url = data.get('url')
        
        if not video_url:
            return "ဗီဒီယို Link မရှိပါ"

        # AI ကို ခိုင်းတဲ့အပိုင်း (Gemini Model)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"Please summarize this video content in Burmese language: {video_url}. Give me the main points clearly."
        
        response = model.generate_content(prompt)
        
        # AI ဆီက ရလာတဲ့ မြန်မာလို အနှစ်ချုပ်ကို App ဆီ ပြန်ပို့ခြင်း
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
