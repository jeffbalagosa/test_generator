# Test Generator

A simple quiz application that generates tests from Quizlet export data.

## Installation

1. Clone the repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment: `.venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements-dev.txt`

## Usage

Run the main application:
```bash
python main.py
```

## Testing

Run the unit tests:
```bash
python -m pytest tests/
```

## Features

- Loads quiz data from Quizlet export files
- Generates multiple choice questions
- Tracks score and incorrect questions
- Detects internet connection (cheating prevention)
