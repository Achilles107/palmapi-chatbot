from flask import Flask, render_template, request
import google.generativeai as palm
from dotenv import load_dotenv
import os

app = Flask(__name__)
messages = []

load_dotenv()
PALM_KEY = os.getenv('PALM_KEY')
palm.configure(api_key=PALM_KEY)

@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        input_text = request.form.get('input_text')
        user_message = {'sender': 'You', 'content': input_text}
        messages.append(user_message)
        
        reply = palm.chat(context="Behave like a royal Princess. And If someone asks your name, say 'Princess Alice: Mother of dragons'", messages=input_text)
        reply_message = {'sender': 'Princess Alice', 'content': reply.last}
        messages.append(reply_message)

    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run()
