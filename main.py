from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/recap', methods=['POST'])
def do_recap():
    # App ဆီက ပို့လိုက်တဲ့ URL ကို လက်ခံခြင်း
    data = request.json
    video_url = data.get('url')
    
    # စမ်းသပ်ရန်အတွက် Google ကိုပဲ ခဏပြန်ညွှန်းပေးထားမယ်
    # နောက်မှ တကယ့် AI Recap Link နဲ့ လဲပါမယ်
    return "https://www.google.com"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
  
