from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from chatbot import respond

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = respond(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
