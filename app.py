from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__)

@app.route('/detection-api', methods=['GET', 'POST'])
def dectect():
    if request.method == 'GET':
        return render_template("index.html")
        # return jsonify({'response': "Welcome to the twitter object detection api"})

    
    

if __name__ == '__main__':
    app.run(debug=True)