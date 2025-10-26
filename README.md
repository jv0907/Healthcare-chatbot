# Healthcare Chatbot

A simple web-based healthcare chatbot that provides basic medical advice based on user symptoms.

## Features

- Interactive chat interface
- Quick responses for common symptoms
- Modern and responsive UI
- Easy to use and understand
- Mobile-friendly design

## Tech Stack

- Frontend: HTML, CSS
- Backend: Python (Flask)
- Dependencies: Flask

## Installation

1. Clone the repository
```bash
git clone [your-repo-url]
cd healthcare-chatbot
```

2. Create a virtual environment
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies
```bash
pip install Flask
```

## Project Structure

```
Healthcare chatbot/
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── app.py
└── README.md
```

## Running the Application

1. Activate the virtual environment
```bash
.\venv\Scripts\activate
```

2. Run the Flask application
```bash
python app.py
```

3. Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## Usage

1. Type your symptoms in the chat input
2. The chatbot will respond with basic medical advice
3. Currently responds to keywords like:
   - fever
   - headache
   - cough
   - stomach
   - pain
   - tired/fatigue
   - cold

## Notes

- This is a basic rule-based chatbot
- For serious medical conditions, always consult a healthcare professional
- This tool is for educational purposes only

## License

[Your chosen license]

## Author

[Your name]

