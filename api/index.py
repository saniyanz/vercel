import json
from urllib.parse import urlparse, parse_qs

# Load student marks from the JSON file
with open('q-vercel-python.json') as f:
    students_marks = json.load(f)

def handler(event, context):
    # Parse query parameters from the event
    query_params = event.get("queryStringParameters", {})
    names = query_params.get("name", [])
    if not isinstance(names, list):
        names = [names]

    # Fetch marks for the given names
    marks = [students_marks.get(name, "Not Found") for name in names]

    # Build the response
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",  # Enable CORS
        },
        "body": json.dumps({"marks": marks}),
    }
    return response

