"""
Flask API for the AI-Powered Customer Support Email Generator.
Provides endpoints for generating professional email responses to customer complaints.
"""

import os
import yaml
import logging
from datetime import datetime
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load configuration
def load_config():
    """Load configuration from config.yaml"""
    try:
        with open('config.yaml', 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        logging.error("config.yaml not found!")
        return None

config = load_config()

# Configure Gemini AI
if config and config.get('gemini', {}).get('api_key'):
    genai.configure(api_key=config['gemini']['api_key'])
    model = genai.GenerativeModel(config['gemini']['model'])
else:
    logging.error("Gemini API key not found in config!")
    model = None

# Setup logging
logging.basicConfig(
    level=getattr(logging, config.get('logging', {}).get('level', 'INFO')),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/generate_email', methods=['POST'])
def generate_email():
    """Generate professional email response from customer complaint"""
    try:
        # Get complaint text from request
        data = request.get_json()
        if not data or 'complaint' not in data:
            return jsonify({'error': 'No complaint text provided'}), 400
        
        complaint_text = data['complaint'].strip()
        if not complaint_text:
            return jsonify({'error': 'Complaint text cannot be empty'}), 400
        
        # Check if model is available
        if not model:
            return jsonify({'error': 'AI model not available. Please check configuration.'}), 500
        
        # Create prompt for email generation
        prompt = f"""
        You are a professional customer service representative. Please generate a polite, helpful, and professional email response to the following customer complaint.

        The email should:
        - Acknowledge the customer's concern
        - Show empathy and understanding
        - Provide a helpful solution or next steps
        - Maintain a professional and friendly tone
        - Be concise but thorough
        - Include a proper greeting and closing

        Customer Complaint:
        {complaint_text}

        Please generate only the email response without any additional commentary or formatting markers.
        """
        
        # Generate response using Gemini
        response = model.generate_content(
            prompt,
            generation_config={
                'temperature': config['gemini'].get('temperature', 0.7),
                'max_output_tokens': config['gemini'].get('max_output_tokens', 1000),
                'top_p': config['gemini'].get('top_p', 0.9),
                'top_k': config['gemini'].get('top_k', 40),
            }
        )
        
        if response and response.text:
            generated_email = response.text.strip()
            
            # Log successful generation
            logging.info(f"Successfully generated email response for complaint: {complaint_text[:50]}...")
            
            return jsonify({
                'success': True,
                'email': generated_email,
                'timestamp': datetime.now().isoformat()
            })
        else:
            logging.error("No response generated from Gemini API")
            return jsonify({'error': 'Failed to generate email response'}), 500
            
    except Exception as e:
        logging.error(f"Error generating email: {str(e)}")
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    # Create logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)
    
    # Run the app
    host = config.get('api', {}).get('host', '127.0.0.1')
    port = config.get('api', {}).get('port', 5000)
    debug = config.get('api', {}).get('debug', True)
    
    print(f"Starting AI-Powered Customer Support Email Generator...")
    print(f"Server running at http://{host}:{port}")
    
    app.run(host=host, port=port, debug=debug)


