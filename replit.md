# Bulk SMS Broadcasting App

## Overview

This is a Flask-based web application that enables users to send bulk SMS messages to multiple recipients using Africa's Talking SMS API. The application supports both manual phone number entry and CSV file uploads, with a clean Bootstrap-powered frontend interface.

## User Preferences

Preferred communication style: Simple, everyday language.
Phone number format: Ghana numbers (+233) instead of Kenya numbers.

## System Architecture

The application follows a traditional server-side web architecture pattern:

- **Backend**: Python Flask web framework serving HTML templates and handling API requests
- **Database**: PostgreSQL database for storing SMS campaigns, delivery records, and statistics
- **Frontend**: Server-side rendered HTML with Bootstrap CSS framework and vanilla JavaScript
- **SMS Integration**: Africa's Talking API for SMS delivery
- **File Processing**: Server-side CSV parsing for bulk phone number uploads
- **Deployment**: Configured for containerized deployment with proxy support

## Key Components

### Backend Components

1. **Flask Application (`app.py`)**
   - Main application entry point with route handlers
   - Database models and SQLAlchemy configuration
   - Session management with secret key configuration
   - Proxy middleware support for production deployment
   - Form data processing and validation
   - Campaign management and statistics tracking

2. **SMS Service (`sms_service.py`)**
   - Encapsulates Africa's Talking API integration
   - Handles single SMS sending with error handling
   - Manages API credentials through environment variables
   - Provides structured response handling

3. **Utilities (`utils.py`)**
   - Phone number validation and formatting (Ghana format: +233XXXXXXXXX)
   - CSV file parsing functionality
   - Input sanitization and cleaning

4. **Entry Point (`main.py`)**
   - Development server configuration
   - Debug mode enabled for development

### Frontend Components

1. **HTML Templates (`templates/index.html`)**
   - Bootstrap 5-based responsive design
   - Form interface for message composition
   - Support for both text input and CSV file upload
   - Progress tracking and results display sections

2. **CSS Styling (`static/css/style.css`)**
   - Custom styling with CSS variables
   - Gradient backgrounds and modern card design
   - Responsive layout optimization
   - Hover effects and transitions

3. **JavaScript (`static/js/app.js`)**
   - Client-side form validation
   - Real-time character and SMS part counting
   - CSV file handling
   - Progress tracking and results display

## Data Flow

1. **Message Composition**: User enters message and phone numbers via web interface
2. **Input Processing**: Server validates and cleans phone numbers, processes CSV uploads
3. **Campaign Creation**: New SMS campaign record created in database
4. **SMS Dispatch**: Messages sent through Africa's Talking API with database logging
5. **Response Tracking**: Individual SMS delivery status and costs stored in database
6. **Statistics Update**: Daily statistics aggregated and updated
7. **Results Display**: Comprehensive results shown with delivery status per recipient

## External Dependencies

### Python Packages
- **Flask**: Web framework for routing and templating
- **Flask-SQLAlchemy**: Database ORM for PostgreSQL integration
- **africastalking**: Official SDK for Africa's Talking SMS API
- **werkzeug**: WSGI utilities (ProxyFix middleware)
- **psycopg2-binary**: PostgreSQL database adapter

### Frontend Libraries
- **Bootstrap 5.3.0**: UI framework and responsive design
- **Font Awesome 6.4.0**: Icon library
- **Vanilla JavaScript**: No additional frontend frameworks

### SMS Service
- **Africa's Talking API**: SMS delivery service
- Requires API credentials (username and API key)
- Supports Ghana phone number formats (+233XXXXXXXXX)

## Deployment Strategy

The application is configured for flexible deployment:

1. **Development**: Local Flask development server with debug mode
2. **Production**: WSGI-compatible with proxy middleware support
3. **Environment Configuration**: Uses environment variables for sensitive data
4. **Session Security**: Configurable secret key for session management

### Environment Variables Required
- `AFRICAS_TALKING_USERNAME`: API username (defaults to 'sandbox' for testing)
- `AFRICAS_TALKING_API_KEY`: API key for authentication
- `SESSION_SECRET`: Flask session secret key (optional, has fallback)

### SMS Environment Status
- **Current Mode**: Sandbox (testing only - no real SMS delivery)
- **Production Setup**: Requires actual Africa's Talking account credentials
- **Note**: Sandbox mode simulates SMS sending but doesn't deliver to actual phones

### Deployment Considerations
- ProxyFix middleware configured for reverse proxy setups
- Debug mode should be disabled in production
- Environment variables must be properly configured
- File upload limits may need adjustment based on expected CSV sizes

## Database Schema

The application uses PostgreSQL with the following main tables:

- **sms_campaigns**: Campaign metadata (message, recipients, costs, status)
- **sms_records**: Individual SMS delivery records with status and costs
- **invalid_phone_numbers**: Invalid numbers from campaigns for analysis
- **sms_statistics**: Daily aggregated statistics for reporting

The application architecture prioritizes simplicity and reliability, with clear separation between SMS service logic, utility functions, web interface components, and data persistence. The modular design allows for easy testing and maintenance while providing a robust bulk SMS broadcasting solution with comprehensive tracking and analytics.