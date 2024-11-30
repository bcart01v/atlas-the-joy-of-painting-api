import os
from flask import Flask, send_from_directory
from flask_cors import CORS

# Flask app
app = Flask(
    __name__,
    static_folder="../front-facing/static",
    template_folder="../front-facing"
)
CORS(app)  # Enable CORS for the front end

# Route to serve index.html
@app.route("/")
def index():
    return send_from_directory(app.template_folder, "index.html")

# Route to serve static files (JS, CSS)
@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5005, debug=True)