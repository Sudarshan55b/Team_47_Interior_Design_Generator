# Interior Design Generator

## Overview
The **Interior Design Generator** is a web application that provides AI-generated room layout descriptions and decoration recommendations based on user preferences. 
Users can input details such as room type, style, color scheme, and furniture preferences to receive detailed design suggestions.

## Features
- **User-Friendly Web Interface**: Interactive web UI for users to input design preferences.
- **AI-Powered Recommendations**: Uses an AI model to generate personalized interior design suggestions.
- **FastAPI Backend**: Implements FastAPI for handling API requests.
- **Asynchronous API Calls**: Uses `httpx` for efficient AI model communication.
- **Copy to Clipboard**: Allows users to copy generated recommendations.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript (Jinja2 templates)
- **Backend**: FastAPI
- **AI Model**: API-based model from `chat.ivislabs.in`
- **HTTP Requests**: `httpx` for making API calls

## Installation & Setup
### Prerequisites
- Python 3.8+
- FastAPI
- Uvicorn
- Jinja2
- httpx

## File Structure
```
interior-design-generator/
│-- static/             # Static files (CSS, images, etc.)
│-- templates/          # Jinja2 HTML templates
│   ├── index.html      # Main web UI
│-- main.py             # FastAPI backend
│-- requirements.txt    # List of dependencies
│-- README.md           # Project documentation
```

## Usage
1. Open the web application.
2. Enter the room type, style, color scheme, and furniture details.
3. Click "Generate Design" to receive AI-generated recommendations.
4. Copy the results to the clipboard if needed.

## API Endpoints
- **GET `/`**: Serves the web UI.
- **POST `/generate_design`**: Accepts form data and returns design recommendations.

## Notes
- Ensure you replace `API_KEY` in `main.py` with a valid API key.
- Customize styles in `static/style.css` if needed.


