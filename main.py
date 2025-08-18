
from flask import Flask, request, jsonify, render_template
from AI_logic import give_response
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('home.html')
    
if __name__ == '__main__':
   app.run(debug=True)