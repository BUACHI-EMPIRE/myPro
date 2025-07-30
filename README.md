# Bulk SMS Broadcasting Application

## Overview
This is a Flask-based web application for sending bulk SMS messages to multiple recipients. It uses Africa's Talking API for SMS delivery and provides a user-friendly interface for composing messages, managing campaigns, and viewing statistics.

## Features
- Send SMS messages to multiple recipients at once
- Upload phone numbers via CSV file or manual entry
- Track delivery status of each message
- View campaign statistics and history
- Validate phone numbers before sending
- Responsive design for desktop and mobile use

## Requirements
- Python 3.7+
- Flask
- SQLAlchemy
- Africa's Talking API account

## Installation

1. Clone the repository:
```
git clone <repository-url>
cd SMSFlask
```

2. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Set up environment variables:
```
export AFRICAS_TALKING_USERNAME="your_username"  # On Windows: set AFRICAS_TALKING_USERNAME=your_username
export AFRICAS_TALKING_API_KEY="your_api_key"    # On Windows: set AFRICAS_TALKING_API_KEY=your_api_key
export DATABASE_URL="sqlite:///sms_app.db"       # Optional: defaults to SQLite
export SESSION_SECRET="your_secret_key"          # Optional: for session security
```

## Running the Application

1. Start the Flask development server:
```
python main.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

## Usage

1. **Compose Message**: Enter your SMS message in the text area.
2. **Add Recipients**: Enter phone numbers manually (one per line) or upload a CSV file.
3. **Send Messages**: Click the "Send SMS Messages" button to broadcast your message.
4. **View Results**: See delivery status and statistics for your campaign.
5. **Campaign History**: Access past campaigns from the Campaigns menu.
6. **Statistics**: View overall usage statistics from the Statistics menu.

## Phone Number Format

The application is configured for Ghana phone numbers in the following formats:
- +233XXXXXXXXX (international format with plus)
- 233XXXXXXXXX (international format without plus)
- 0XXXXXXXXX (local format with leading zero)
- XXXXXXXXX (local format without leading zero)

All numbers are converted to the international format (+233XXXXXXXXX) before sending.

## Development

### Project Structure
- `main.py`: Application entry point
- `app.py`: Flask application and routes
- `sms_service.py`: SMS sending functionality
- `utils.py`: Utility functions for phone number handling
- `templates/`: HTML templates
- `static/`: CSS, JavaScript, and other static files

### Database
The application uses SQLAlchemy with SQLite by default. You can configure a different database by setting the `DATABASE_URL` environment variable.

## License
This project is licensed under the MIT License - see the LICENSE file for details.