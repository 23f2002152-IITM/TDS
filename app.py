from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask import CORS
import json

app = Flask(__name__)
CORS(app)

marks_db = json.load(open('q-vercel-python.json'))

@app.route('/api',methods=['GET'])
def index():
    names = request.args.getlist('name')
    results = []
    for i in marks_db:
        if i['name'] in names:
            results.append(i['marks'])
    return jsonify({'marks':results})
    # return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

