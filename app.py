from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

marks_db = json.load(open('q-vercel-python.json'))

@app.route('/api', methods=['GET'])
def index():
    names = request.args.getlist('name')
    name_to_marks = {entry['name']: entry['marks'] for entry in marks_db}
    results = [name_to_marks[name] for name in names if name in name_to_marks]
    return jsonify({'marks': results})

    # return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

