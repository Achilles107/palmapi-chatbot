from flask import Flask, render_template, request
import google.generativeai as palm

app = Flask(__name__)
messages = []

PALM_KEY = 'AIzaSyBg_mbXxMU-lnYjJ9ow29QZc4cEx2dju7s'
palm.configure(api_key=PALM_KEY)

@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        input_text = request.form.get('input_text')
        user_message = {'sender': 'You', 'content': input_text}
        messages.append(user_message)
        
        reply = palm.chat(context="Be a Cowboy", messages=input_text)
        reply_message = {'sender': 'ChatBot', 'content': reply.last}
        messages.append(reply_message)

    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run()
