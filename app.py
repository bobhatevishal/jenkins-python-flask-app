from flask import Flask, jsonify, render_template_string
import logging

app = Flask(__name__)

# Enable logging
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    app.logger.info("Home page accessed.")
    return render_template_string("""
        <!doctype html>
        <html>
        <head>
            <title>Flask + Jenkins + Docker</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; background: #f5f5f5; margin-top: 100px; }
                h1 { color: #2e86de; }
                p  { font-size: 1.2rem; }
            </style>
        </head>
        <body>
            <h1>🚀 CI/CD Flask App</h1>
            <p>Deployed with Jenkins + Docker on port 5000!</p>
        </body>
        </html>
    """)

@app.route("/health")
def health():
    return jsonify(status="UP"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

