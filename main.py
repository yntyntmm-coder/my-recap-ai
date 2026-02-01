import os
import google.generativeai as genai
from flask import Flask, request

# --- (၁) မင်းရဲ့ Gemini API Key ကို အောက်က မျက်တောင်ဖွင့်ပိတ်ထဲမှာ ထည့်ပါ ---
API_KEY = "မင်းရဲ့_API_Key_ကို_ဒီမှာထည့်" 
# ------------------------------------------------------------------

# Gemini AI ကို အလုပ်လုပ်ဖို့ ပြင်ဆင်ခြင်း
genai.configure(api_key=API_KEY)
app = Flask(__name__)

# အိမ်ရှေ့ (Home Page) အတွက် Code - ဒါက မင်းအခု မြင်နေရတဲ့ HTML နေရာပါ
@app.route('/')
def home():
    return "AI Recap Server is Running!"

# အခန်းထဲ (Recap Route) အတွက် Code - ဒါက တကယ့် AI အလုပ်လုပ်တဲ့နေရာပါ
@app.route('/recap', methods=['POST'])
def do_recap():
    try:
        # App က ပို့လိုက်တဲ့ YouTube Link ကို ယူခြင်း
        data = request.json
        video_url = data.get('url')
        
        if not video_url:
            return "ဗီဒီယို Link မရှိပါဘူးဗျာ။"

        # AI (Gemini 1.5 Flash) ကို ခိုင်းစေခြင်း
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # AI ကို ခိုင်းမယ့် စာသား (Prompt)
        prompt = f"Please summarize this YouTube video content in Burmese language: {video_url}. Give me a clear and detailed summary."
        
        response = model.generate_content(prompt)
        
        # AI ရဲ့ အဖြေကို App ဆီ ပြန်ပို့ခြင်း
        return response.text

    except Exception as e:
        # Error တက်ရင် ဘာကြောင့်လဲဆိုတာ ပြန်ပြောပြခြင်း
        return f"Error တက်သွားတယ်ဗျ: {str(e)}"

if __name__ == "__main__":
    # Render အတွက် Port နံပါတ် သတ်မှတ်ခြင်း
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
