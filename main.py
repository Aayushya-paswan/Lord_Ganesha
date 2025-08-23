from speech_to_text import speech_to_text, text_to_speech
from flask import Flask, request, jsonify, render_template
from gem import generate_gemini_response as give_response
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('home.html')

@app.route('/handle', methods=['POST'])
def take_input():
   text = speech_to_text()
   if text:
      response = give_response(text)
      text_to_speech(response)
      return jsonify({'response': response})
   else:
       return jsonify({'response': 'Sorry, I did not understand that.'})
    
if __name__ == '__main__':
   app.run(debug=True)