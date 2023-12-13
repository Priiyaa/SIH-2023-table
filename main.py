from flask import Flask, render_template
app=Flask(__name__)

headings=("Col1","Col2","Col3","Col4","Col5","Col6")

data=(
  
("Col enteries",	"Col enteries",	"Col enteries","Col enteries",	"Col enteries",	"Col enteries"),
("Col enteries 2",	"Col enteries 2",	"Col enteries 2","Col enteries",	"Col enteries",	"Col enteries"),
("Col enteries 3"	,"Col enteries 3"	,"Col enteries 3","Col enteries 3"	,"Col enteries 3"	,"Col enteries 3"),
("Col enteries 3"	,"Col enteries 3"	,"Col enteries 3","Col enteries 3"	,"Col enteries 3"	,"Col enteries 3"),
("Col enteries 3"	,"Col enteries 3"	,"Col enteries 3","Col enteries 3"	,"Col enteries 3"	,"Col enteries 3"),

)
@app.route("/")
def home():
    return render_template('index.html',headings=headings,data=data)