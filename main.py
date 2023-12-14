# import openai
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, session
# from flask_bootstrap import Bootstrap


app = Flask(__name__)
# load_dotenv()
# app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
# Bootstrap(app)
headings=("Col1","Col2","Col3","Col4","Col5","Col6")

data=(
  
("Col enteries",	"Col enteries",	"Col enteries","Col enteries",	"Col enteries",	"Col enteries"),
("Col enteries 2",	"Col enteries 2",	"Col enteries 2","Col enteries",	"Col enteries",	"Col enteries"),
("Col enteries 3"	,"Col enteries 3"	,"Col enteries 3","Col enteries 3"	,"Col enteries 3"	,"Col enteries 3"),
("Col enteries 3"	,"Col enteries 3"	,"Col enteries 3","Col enteries 3"	,"Col enteries 3"	,"Col enteries 3"),
("Col enteries 3"	,"Col enteries 3"	,"Col enteries 3","Col enteries 3"	,"Col enteries 3"	,"Col enteries 3"),
)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html',headings=headings,data=data)

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    return render_template('chat.html')
@app.route('/new', methods=['GET', 'POST'])
def new():
    return render_template('new.html')
@app.route('/bot', methods=['GET', 'POST'])
def bot():
    return render_template('bot.html')
@app.route('/botnew', methods=['GET', 'POST'])
def botnew():
    return render_template('botnew.html')

if __name__ == "__main__":
    app.run(debug=True)


