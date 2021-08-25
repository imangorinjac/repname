from flask import Flask, render_template
app = Flask(__name__)
from datetime import datetime

@app.route('/')

def home():
    time=datetime.now()

    return render_template('index.html',value=time)

if __name__ == '__main__':
   app.run()