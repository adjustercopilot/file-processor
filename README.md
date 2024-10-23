# File Processor

This API processes various types of document files (PDF, DOCX, TXT, PPTX, CSV, JSON) to extract structured insurance claim information. It utilizes Google Generative AI to analyze the content and return the relevant data in a structured JSON format.

## Features

- **Multiple File Support:** Upload and process various document formats including PDF, DOCX, TXT, PPTX, CSV, and JSON.
- **Structured Data Extraction:** Extract relevant insurance claim information and return it in a structured JSON format.
- **Error Handling:** Handle various document types with appropriate error messages.
- **CORS Support:** Enable cross-origin requests for easier integration.

## Installation

1. **Clone this repository:**

   ```bash
   git clone https://github.com/adjustercopilot/file-processor.git
   cd file-processor

   ```

2. **Create a virtual environment:**

- **For Windows**

  ```bash
  python -m venv venv
  cd venv\Scripts\activate

  ```

- **For macOS/Linux:**

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt

   ```

4. **Configure Environment Variables:**

- Create a .env file in the project root and add your Google API key.
  GOOGLE_API_KEY=your_api_key_here

## API Endpoints:

POST /api/template/generate

- This endpoint processes uploaded files and extracts structured data.

**Request Body:**

- uploaded_files: A list of files to be processed (PDF, DOCX, TXT, PPTX, CSV, JSON).

**Response:**

- Returns a JSON response containing the extracted file information.

## Usage

1. **Start the FastAPI server:**

   ```bash
   uvicorn main:app --reload

   ```

2. Navigate to http://localhost:8000/ to access the interactive API documentation

3. Upload files using the /api/template/generate endpoint to extract claim information.
