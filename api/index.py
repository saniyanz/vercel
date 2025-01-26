from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

# Load the student marks from the JSON file
with open(q-vercel-python.json') as f:
    students_marks = json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')  # Get list of names from query parameters
    marks = []

    for name in names:
        marks.append(students_marks.get(name, "Not Found"))  # Return "Not Found" if name is not in dictionary

    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run(debug=True)
