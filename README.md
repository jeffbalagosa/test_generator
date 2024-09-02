# Quiz Application

This is a Python-based quiz application that tests users on various questions and answers derived from a structured dataset. The application features a set of questions with multiple choice answers and checks for internet connection to prevent cheating.

## Features

- **Data Formatting**: Converts raw data into a structured format for quiz administration.
- **Randomized Questions and Answers**: Randomly selects questions and shuffles answer choices.
- **Cheating Prevention**: Detects internet connection during the quiz to prevent cheating.
- **Scoring**: Calculates and displays the user's score at the end of the quiz.

## Installation

1. Ensure you have Python installed on your system.
2. Clone this repository or download the source code.

```sh
git clone <repository-url>
cd <repository-directory>
```

3. Run the main script.

```sh
python main.py
```

## Usage

Upon running the script, the application will:

1. Print the current date and time.
2. Administer a series of questions from the provided dataset.
3. Detect if there is an internet connection to prevent cheating.
4. Display the user's score at the end of the quiz.

### Example

```sh
$ python main.py
Test administered on 2024-06-19 15:45:30

1) Who was the author of the problem-solving approach discussed in the first chapter?
A. Charles
B. Canon
C. Logic tree
D. Seven

Enter the number of your answer: A

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

## Contributing

If you want to contribute to this project, please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any questions or suggestions, please open an issue in the repository.
