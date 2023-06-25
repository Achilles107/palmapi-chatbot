from flask import Flask, render_template, request

app = Flask(__name__)
messages = []

@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        input_text = request.form.get('input_text')
        user_message = {'sender': 'You', 'content': input_text}
        messages.append(user_message)

        reply_message = {'sender': 'ChatBot', 'content': input_text + 'Z'}
        messages.append(reply_message)

    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run()
