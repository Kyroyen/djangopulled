# Live Transcription ASGI Django Project Documentation

## Overview
This documentation provides an overview and guide for setting up a small ASGI (Asynchronous Server Gateway Interface) Django project for live transcription using modules such as Daphne, Channels, and OpenAI Whisper. The project includes an HTTP index page and a WebSocket route for live translation.

## Requirements
- Python (>=3.6)
- Django (>=3.0)
- Daphne
- Channels
- OpenAI Whisper
- A compatible web browser

## Installation
1. Clone the project repository from GitHub:
    ```
    git clone git@github.com:Kyroyen/liveTranscriptionWhisperAPI-.git
    ```

2. Install project dependencies using pip:
    ```
    cd stream
    pip install -r requirements.txt
    ```

## Configuration
1. Set up Django settings:
    - Make sure `django.contrib` and `channels` apps are added to `INSTALLED_APPS`.
    - Configure `ASGI_APPLICATION` in `settings.py` to point to the ASGI application.

2. Configure Whisper API:
    - Obtain Whisper API credentials from OpenAI.
    - Store the credentials securely. (e.g., in environment variables)

## Usage
1. Run the ASGI server using Daphne:
    ```
    daphne -p 8000 stream.asgi:application
    ```

2. Access the index page:
    - Open a web browser and navigate to locally : `http://localhost:8000/`; deployment : `https://livetranscriptionwhisperapi.onrender.com/`

3. Start the live transcription:
    - Click the start transcript button to start, stop to end.
    - Alternatively connect to websocket at locally : `ws://localhost:8000/listen`; deployment : `wss://livetranscriptionwhisperapi.onrender.com/listen`

4. Connect to WebSocket for live translation:
    - Utilize the WebSocket route provided by the project to receive live translation updates.

## Project Structure
```
stream/
├── transcript/
│   ├── __init__.py
│   ├── asgi.py
│   ├── consumers.py
│   ├── routing.py
│   ├── templates/
│   │   └── index.html
│   ├── tests.py
│   └── views.py
├── stream/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .gitignore
├── manage.py
└── requirements.txt
```

## Components

### Django App (`transcript`)
- `asgi.py`: ASGI application for handling WebSocket connections.
- `consumers.py`: Consumers for WebSocket connections handling live transcription and translation.
- `routing.py`: URL routing for WebSocket connections.
- `templates/index.html`: HTML template for the index page.
- `views.py`: Views for serving HTTP requests.

### Django Project (`stream`)
- `asgi.py`: ASGI application entry point.
- `settings.py`: Django settings configuration.
- `urls.py`: URL routing for HTTP requests.
- `wsgi.py`: WSGI application entry point.


## Support and Contributions
For any issues or feature requests, please refer to the project's GitHub repository. Contributions via pull requests are welcomed.

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Credits
This project utilizes various open-source libraries and technologies, including Django, Daphne, Channels, and OpenAI Whisper. We express gratitude to the developers and contributors of these projects for their invaluable work.

## Disclaimer
This project is for demonstration purposes only. Ensure compliance with applicable laws and regulations when using live transcription and translation services.