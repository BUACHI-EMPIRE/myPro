#!/usr/bin/env python
"""
Run script for the Bulk SMS Broadcasting Application.
This script sets up the environment and starts the Flask server.
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Check if database exists, if not, initialize it
if not os.path.exists("sms_app.db") and os.environ.get("DATABASE_URL", "").startswith("sqlite"):
    print("Database not found. Initializing...")
    try:
        from init_db import init_db
        init_db()
    except Exception as e:
        print(f"Error initializing database: {e}")
        sys.exit(1)

# Import and run the application
from main import app

if __name__ == "__main__":
    # Get port from environment variable or use default 5000
    port = int(os.environ.get("PORT", 5000))
    
    # Get debug mode from environment variable or use default True
    debug = os.environ.get("FLASK_DEBUG", "True").lower() == "true"
    
    print(f"Starting Bulk SMS Broadcasting Application on port {port}")
    print(f"Debug mode: {'enabled' if debug else 'disabled'}")
    print("Press Ctrl+C to stop the server")
    
    # Run the application
    app.run(host="0.0.0.0", port=port, debug=debug)