import http.server
import json
from urllib.parse import urlparse, parse_qs

# Load student marks from the JSON file
with open('q-vercel-python.json') as f:
    students_marks = json.load(f)

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Enable CORS
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")  # Allow any origin
        self.end_headers()

        # Parse query parameters
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)

        # Get the names from the query parameters
        names = query_params.get("name", [])
        marks = [students_marks.get(name, "Not Found") for name in names]

        # Respond with the marks in the required format
        response = {"marks": marks}
        self.wfile.write(json.dumps(response).encode("utf-8"))

# Export handler to be used by Vercel
handler = CORSRequestHandler

