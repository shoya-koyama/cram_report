from nltk.chat.util import Chat, reflections
from flask import Flask, render_template, request
from yourapplication import app as application

pairs = [
    ['my name is (.*)', ['Hi %1']],
    ['hi|hello|hey', ['Hello!', 'Hi there!']],
    ['what is your name?', ['My name is Bot.']],
    ['how are you?', ['I am doing well.', 'I am fine, thank you.']],
    ['what can you do?', ['I can assist you in various ways.']],
    ['bye|goodbye', ['Goodbye!', 'Have a nice day!']],
]

# NLTKのChatオブジェクトを作成
chatbot = Chat(pairs, reflections)

# Flaskアプリケーションを作成
app = Flask(__name__)

# ホームページを表示するルート
@app.route('/')
def home():
    return render_template('indexbot.html')

# チャットボットの応答を受け取るAPI
@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    reply = chatbot.respond(message)
    return str(reply)

if __name__ == '__main__':
    app.run()