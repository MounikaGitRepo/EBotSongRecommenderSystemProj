
import ebot
from flask import Flask, render_template, request,jsonify


app = Flask(__name__)
app.static_folder = 'static'


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user=request.args.get("msg").lower()
    d=ebot.get_resp(user)
   
    return jsonify(d)
    
    
if __name__ == "__main__":
    app.run() 