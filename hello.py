from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def my_name():
    return 'Haja Fatou Nje '


@app.route('/')
def my_email():
    return 'hajafatounjie@gmail.com'

if __name__=="__main__":
   app.run(debug=True)
