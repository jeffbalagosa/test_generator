# Quiz Generator

This is a Python-based quiz generator that creates interactive multiple-choice quizzes from Quizlet export files. The application parses structured text files containing question-answer pairs and administers randomized quizzes with cheating prevention features.

## Features

- **Quizlet Export Parsing**: Reads and parses Quizlet export files with custom delimiters (`{-tab-}` for term-definition separation, `{-line_break-}` for pair separation).
- **Randomized Questions and Answers**: Randomly selects questions and shuffles multiple-choice answer options.
- **Cheating Prevention**: Detects internet connection during the quiz to prevent cheating.
- **Scoring and Feedback**: Calculates and displays the user's score with percentage and lists incorrect questions.
- **Configurable Quiz Length**: Administers up to 10 questions by default, or all available questions if fewer exist.

## Installation

1. Ensure you have Python 3.11+ installed on your system.
2. Clone this repository or download the source code.

```sh
git clone <repository-url>
cd <repository-directory>
```

3. Install development dependencies (optional, for testing and linting):

```sh
pip install -r requirements-dev.txt
```

## Usage

The application is configured to read from a specific Quizlet export file (`tests/micah/12-rules.txt`). To use with your own quiz data:

1. Export your Quizlet set as a text file.
2. Replace the content in `tests/micah/12-rules.txt` with your exported data, ensuring the format uses:
   - `{-tab-}` to separate terms from definitions
   - `{-line_break-}` to separate question-answer pairs

3. Run the main script:

```sh
python main.py
```

Upon running the script, the application will:

1. Print the current date and time.
2. Administer a series of multiple-choice questions from the loaded dataset.
3. Detect internet connection to prevent cheating.
4. Display the user's score and list of incorrect questions at the end.

### Example Output

```sh
Test administered on 2024-06-19 15:45:30

1) Rule #1
A. Stand Tall. Be confident in yourself. Standing up straight with your shoulders back helps you feel strong and ready for anything. It also shows others that you believe in yourself.
B. Take Care of Yourself. Treat yourself with kindness. Make sure you eat well, get enough sleep, and do things you enjoy. Just like you would take care of a good friend, it's important to take care of yourself.
C. Choose Good Friends. Surround yourself with positive people. Good friends are those who make you feel happy and support your goals. Stay away from those who bring you down or get you into trouble.
D. Get Better Every Day. Focus on your own growth. Instead of comparing yourself to others, try to be a little better than you were yesterday. Small improvements add up over time.

Enter the letter of your answer: A

Correct!

2) What does it mean to "stand tall" in a tough situation?
...
```

## File Format

The input file must follow this exact format:
```
Term1{-tab-}Definition1{-line_break-}Term2{-tab-}Definition2{-line_break-}
```

Each pair consists of a term (question) and definition (correct answer), separated by `{-tab-}`. Pairs are separated by `{-line_break-}`.

## Development

- Run tests: `pytest`
- Lint code: `flake8`
- Format code: `black .`

## Requirements

- Python 3.11+
- No external dependencies for core functionality

2) Which company did Charles intern at in Japan?
A. Canon
B. Sydney Airport
C. Logic trees
D. Charles

Enter the number of your answer: A

...

Score: 8/10 (80.00%)
```

## Files

- `main.py`: The main script that runs the quiz application.
- `config.py`: Configuration file containing the quiz questions and answers data.

## Contributing

If you want to contribute to this project, please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any questions or suggestions, please open an issue in the repository.
