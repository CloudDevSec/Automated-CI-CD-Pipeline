from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is the Sample App by Sascha!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
