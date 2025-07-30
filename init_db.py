#!/usr/bin/env python
"""
Database initialization script for the Bulk SMS Broadcasting Application.
Run this script to create the initial database tables.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def init_db():
    """Initialize the database by creating all tables."""
    from app import app, db
    
    with app.app_context():
        # Create all tables
        db.create_all()
        print("Database tables created successfully!")

        # Print database URL (without sensitive information)
        db_url = app.config["SQLALCHEMY_DATABASE_URI"]
        if "://" in db_url:
            # Hide password if present
            parts = db_url.split("://")
            if "@" in parts[1]:
                auth, rest = parts[1].split("@", 1)
                if ":" in auth:
                    user = auth.split(":", 1)[0]
                    masked_url = f"{parts[0]}://{user}:****@{rest}"
                else:
                    masked_url = f"{parts[0]}://{auth}@{rest}"
            else:
                masked_url = db_url
        else:
            masked_url = db_url
            
        print(f"Using database: {masked_url}")

if __name__ == "__main__":
    init_db()