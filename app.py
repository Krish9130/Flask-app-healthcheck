from flask import Flask, request, jsonify
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

# Create a Flask application
app = Flask(__name__)

# Configure logging
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.DEBUG)  # Enable all log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)

# Log with custom levels and timestamp
def log_with_timestamp(message, level="info"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"{timestamp} - {message}"
    if level == "debug":
        app.logger.debug(log_message)
    elif level == "info":
        app.logger.info(log_message)
    elif level == "warning":
        app.logger.warning(log_message)
    elif level == "error":
        app.logger.error(log_message)
    elif level == "critical":
        app.logger.critical(log_message)

# Home route
@app.route('/')
def home():
    log_with_timestamp('Home page accessed - Status: 200 OK', "info")
    return "Welcome to the DevOps Team Sangachadwam", 200

# Health check route
@app.route('/health', methods=['GET'])
def health_check():
    log_with_timestamp('Health check accessed - Status: 200 OK', "info")
    response = {
        "status": "UP",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return jsonify(response), 200

# Log all incoming requests
@app.before_request
def log_request_info():
    log_with_timestamp(f"Request: {request.method} {request.path}", "info")

# Handle favicon requests to prevent unnecessary errors
#@app.route('/favicon.ico')
#def favicon():
#    return '', 204  # Return a no-content response

# Handle 404 errors (route not found)
@app.errorhandler(404)
def page_not_found(e):
    log_with_timestamp(f"404 Not Found: {request.path} accessed", "warning")
    return jsonify({"error": "Page not found", "status": 404}), 404

# Handle general exceptions globally
@app.errorhandler(Exception)
def handle_exception(e):
    log_with_timestamp(f"Unhandled exception occurred: {str(e)}", "critical")
    return jsonify({"error": "An unexpected error occurred", "status": 500}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)


