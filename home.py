from flask import Flask, render_template,request,flask
app = Flask(__name__)

name=request.form('name')
@app.route('/',methods=['GET','POST'])

def home():
  
    return render_template('index.html',name=name)

if __name__ == '__main__':
   app.run()