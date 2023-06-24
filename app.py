from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        input_text = request.form.get('input_text')
        modified_text = input_text + 'Z'
        return render_template('index.html', modified_text=modified_text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
