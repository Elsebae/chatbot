import os
from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import time

app = Flask(__name__)
CORS(app)

# Serve static files from root directory
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

# Serve CSS directly
@app.route('/style.css')
def serve_css():
    return send_from_directory('.', 'style.css')

# Serve the main page
@app.route('/')
def home():
    return render_template('index.html')

# Your existing chat endpoint
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'response': 'Please send a message.'}), 400
            
        user_message = data.get('message', '')
        print(f"User: {user_message}")
        
        start_time = time.time()
        response = assistant.get_response(user_message)
        response_time = (time.time() - start_time) * 1000
        
        print(f"Bot: {response[:100]}...")
        print(f"⏱️ Response time: {response_time:.1f}ms")
        
        return jsonify({'response': response})
        
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'response': 'Hello! I\'m GAZA 101. How can I help you today?'})

# Health check
@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

# Initialize assistant (your existing code)
assistant = HybridGazaAssistant()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 7860))
    print(f"🚀 Starting HYBRID GAZA 101 Assistant...")
    print(f"📍 Server running at: http://0.0.0.0:{port}")
    app.run(debug=False, host='0.0.0.0', port=port)
