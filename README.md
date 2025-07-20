# Learning Path Generator with Model Context Protocol (MCP)

This project is a Streamlit-based web application that generates personalized learning paths using the Model Context Protocol (MCP). It integrates with various services including YouTube, Google Drive, and Notion to create comprehensive learning experiences.

## Features

- 🎯 Generate personalized learning paths based on your goals
- 🎥 Integration with YouTube for video content
- 📁 Google Drive integration for document storage
- 📝 Notion integration for note-taking and organization
- 🚀 Real-time progress tracking
- 🎨 User-friendly Streamlit interface

## Prerequisites

- Python 3.10+
- Google ai Studio API Key
- Pipedream URLs for integrations (YouTube and either Drive or Notion)

## Installation

1. Clone the repository:

2. Create and activate a virtual environment:

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Configuration

Before running the application, you'll need to set up:

1. Google API Key
2. Pipedream URLs for:
   - YouTube (required)
   - Google Drive or Notion (based on your preference)

## Running the Application

To start the application, run:
```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501` by default.

## Usage

1. Enter your Google ai studio API key and Pipedream URLs in the sidebar
2. Select your preferred secondary tool (Drive or Notion)
3. Enter your learning goal (e.g., "I want to learn python basics in 3 days")
4. Click "Generate Learning Path" to create your personalized learning plan

## Project Structure

- `app.py` - Main Streamlit application
- `utils.py` - Utility functions and helper methods
- `prompt.py` - Prompt template
- `requirements.txt` - Project dependencies

🚀 MCP MegaWorkshop 2025 – Project Access Details

I’m excited to share the MCP MegaWorkshop 2025 project with you! 🎉
You can access the live app here:

🔗 Project Link:
https://mcp-megaworkshop-2025.streamlit.app/

🔑 Credentials & API Access
Please use the following credentials and API URLs for integration:

🔐 Google API Key:
AIzaSyCo8ciO8_1MuD-gb4jgeg1RhKbj1zLYtmI

🔁 Pipedream Integration URLs:

📺 YouTube API:
https://mcp.pipedream.net/7c74e408-2fed-4cc5-9ed0-49be40ee4d2b/youtube_data_api

📁 Google Drive API:
https://mcp.pipedream.net/7c74e408-2fed-4cc5-9ed0-49be40ee4d2b/google_drive

🧾 Notion API:
https://mcp.pipedream.net/7c74e408-2fed-4cc5-9ed0-49be40ee4d2b/notion

Feel free to explore, test the integrations, and share feedback!
Let me know if you face any issues or need access support.

— Rishabh Tomar

