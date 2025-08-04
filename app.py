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
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>CI/CD Flask App</title>
            <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
            <style>
                body {
                    font-family: 'Poppins', sans-serif;
                    background: linear-gradient(135deg, #74ebd5 0%, #ACB6E5 100%);
                    margin: 0;
                    padding: 0;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                    color: #fff;
                    text-align: center;
                }
                h1 {
                    font-size: 3rem;
                    margin-bottom: 1rem;
                    animation: fadeIn 1s ease-in-out;
                }
                p {
                    font-size: 1.2rem;
                    margin-bottom: 2rem;
                    animation: fadeIn 1.5s ease-in-out;
                }
                .badge {
                    background: #2e86de;
                    padding: 0.6rem 1.2rem;
                    border-radius: 999px;
                    font-weight: bold;
                    font-size: 1rem;
                    box-shadow: 0 4px 14px rgba(0,0,0,0.25);
                    animation: bounce 2s infinite;
                }
                @keyframes fadeIn {
                    from { opacity: 0; transform: translateY(-20px); }
                    to { opacity: 1; transform: translateY(0); }
                }
                @keyframes bounce {
                    0%, 100% { transform: translateY(0); }
                    50% { transform: translateY(-8px); }
                }
            </style>
        </head>
        <body>
            <h1>🚀 Flask CI/CD Deployed</h1>
            <p>Powered by Jenkins + Docker</p>
            <div class="badge">Port: 5000</div>
        </body>
        </html>
    """)

@app.route("/health")
def health():
    app.logger.info("Health check accessed.")
    return jsonify(status="UP"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
