import random
import socket
from datetime import datetime

# Format of the raw data: Each term (or question) and definition (or answer) pair is separated by "{-line_break-}" and the question and answer are separated by "{-tab-}" Example: "Term{-tab-}Definition{-line_break-}"
raw_data = """Question 1{-tab-}Answer 1{-line_break-}Question 2{-tab-}Answer 2{-line_break-}Question 3{-tab-}Answer 3{-line_break-}Question 4{-tab-}Answer 4{-line_break-}Question 5{-tab-}Answer 5{-line_break-}Question 6{-tab-}Answer 6{-line_break-}Question 7{-tab-}Answer 7{-line_break-}Question 8{-tab-}Answer 8{-line_break-}Question 9{-tab-}Answer 9{-line_break-}Question 10{-tab-}Answer 10{-line_break-}Question 11{-tab-}Answer 11{-line_break-}Question 12{-tab-}Answer 12{-line_break-}Question 13{-tab-}Answer 13{-line_break-}Question 14{-tab-}Answer 14{-line_break-}Question 15{-tab-}Answer 15{-line_break-}Question 16{-tab-}Answer 16{-line_break-}Question 17{-tab-}Answer 17{-line_break-}Question 18{-tab-}Answer 18{-line_break-}Question 19{-tab-}Answer 19{-line_break-}Question 20{-tab-}Answer 20{-line_break-}"""


def format_test_data(raw_data):
    pairs = raw_data.split("{-line_break-}")
    formatted_test_data = []
    for pair in pairs:
        if "{-tab-}" in pair:
            term, definition = pair.split("{-tab-}")
            formatted_test_data.append({"term": term, "definition": definition})
    return formatted_test_data


def select_random_items(source_list, count, exclude_indices=set()):
    """
    Selects a specified count of random items from a source list, excluding specified indices.
    """
    available_choices = [i for i in range(len(source_list)) if i not in exclude_indices]
    selected_items = random.sample(
        available_choices, min(count, len(available_choices))
    )
    return selected_items


def get_question_and_answers(formatted_test_data, exclude=set()):
    """
    Generates a question, the correct answer, three wrong answers, and maps answers to letters.
    Excludes questions with indices in the 'exclude' set.
    """
    # Select a random question that is not in the exclude set
    question_indices = select_random_items(formatted_test_data, 1, exclude)
    if not question_indices:
        raise ValueError("No more available questions.")
    question_index = question_indices[0]
    question_data = formatted_test_data[question_index]
    correct_answer = question_data["definition"]

    # Select three wrong answers
    wrong_answer_indices = select_random_items(
        formatted_test_data, 3, exclude.union({question_index})
    )
    wrong_answers = [
        formatted_test_data[idx]["definition"] for idx in wrong_answer_indices
    ]

    # Combine correct and wrong answers, then shuffle
    answers = [correct_answer] + wrong_answers
    random.shuffle(answers)

    # Map answers to letters (A, B, C, D)
    answer_letters = {chr(65 + i): answer for i, answer in enumerate(answers)}

    return question_data["term"], correct_answer, answer_letters, question_index


def prompt_user_question(question, correct_answer, answers):
    """
    Present a question to the user, collect their answer, and check for
    correctness.

    This function displays a question with multiple choice answers, prompts
    the user for their selection, checks for internet connection to prevent
    cheating, and determines if the user's answer is correct.

    Args:
        question (str): The question to be asked.
        correct_answer (str): The correct answer to the question.
        answers (dict): A dictionary of answer choices, with letters as keys
        and answer text as values.

    Returns:
        bool: True if the user's answer is correct, False otherwise.

    Note:
        - The function will continue to prompt the user until a valid answer
        is provided.
        - If an internet connection is detected, a warning message will be
        displayed.
    """
    print(f"{question}\n")
    for letter, answer in answers.items():
        print(f"{letter}. {answer}")

    while True:
        user_answer = input("\nEnter the letter of your answer: ").upper()
        if user_answer in answers:
            break
        else:
            print("Invalid input. Please enter a valid letter.")

    if check_internet_connection():
        print("\033[91m\nInternet connection detected. YOU ARE CHEATING!\n\033[0m")

    if answers[user_answer] == correct_answer:
        return True
    else:
        return False


def check_internet_connection():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False


def administer_test(formatted_test_data, num_questions=10):
    if num_questions > len(formatted_test_data):
        num_questions = len(formatted_test_data)

    num_correct = 0
    percent_correct = 0
    asked_questions = set()
    incorrect_questions = []
    question_number = 1
    print(
        f"\033[92mTest administered on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\033[0m"
    )

    while len(asked_questions) < num_questions:
        question, correct_answer, answers, question_index = get_question_and_answers(
            formatted_test_data, exclude=asked_questions
        )
        if question_index not in asked_questions:
            asked_questions.add(question_index)
            print(f"\n{question_number}) ", end="")
            if prompt_user_question(question, correct_answer, answers):
                num_correct += 1
            else:
                incorrect_questions.append(question_number)
            question_number += 1

    percent_correct = (num_correct / num_questions) * 100
    print(
        f"\033[92mScore: {num_correct}/{num_questions} ({percent_correct:.2f}%)\033[0m"
    )
    if incorrect_questions:
        print(f"Incorrect Questions: {', '.join(map(str, incorrect_questions))}")
    return percent_correct


administer_test(format_test_data(raw_data))
