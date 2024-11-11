# PGM5.py Flask App

This repository contains a simple web application developed with Flask, which displays a counter that can be incremented by clicking a button.

## Features

- Flask web application displaying a counter
- Clicking the "Increment" button increments the counter
- Automatically opens the web browser when the application is launched

## Technologies used

- **Python**: Programming language used to develop the application.
- **Flask**: Python web framework used to create the application.
- **Waitress**: WSGI server used to run the Flask application.

## Requirements

- Python 3.9 or higher
- Flask
- Waitress

## Installation and running

1. Clone the repository:
```
git clone https://github.com/Anggeleo/PGM5.git
```

2. Navigate to the project directory:
```
cd PGM5
```

3. Create and activate a virtual environment (optional, but recommended):
```
python -m venv venv
source venv/bin/activate
```

4. Install the dependencies:
```
pip install -r requirements.txt
```

5. Run the application:
```
python PGM5.py
```

The application will run at `http://127.0.0.1:8080` and will automatically open in your default web browser.

## Using Docker

You can also run the application in a containerized environment using Docker:

1. Build the Docker image:
```
docker build -t pg5-app .
```

2. Run the container:
```
docker run -p 8080:8080 pg5-app
```

The application will run at `http://localhost:8080`.

## Accessing the deployed application on Render

1. Open your web browser.
2. Visit the following URL:
```
https://pgm5.onrender.com
```
3. You will see the Flask application displaying a counter that you can increment by clicking the button.

## Project structure

- `PGM5.py`: Flask application source code
- `Dockerfile`: Dockerfile to build the Docker image
- `requirements.txt`: List of Python dependencies

## Contribution

If you want to contribute to this project, you can follow these steps:

1. Fork the repository.
2. Create a new branch with your changes: `git checkout -b feature/my-new-feature`.
3. Make the necessary changes and update the documentation.
4. Send a pull request explaining your changes.
