from flask import Flask,request,jsonify,render_template
application = Flask(__name__)
app=application
@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)