import random
import socket
from datetime import datetime
from typing import List, Optional, Set

# Path to the Quizlet export file
quizlet_export_file = "quizlet_exports/example.txt"

try:
    with open(quizlet_export_file, "r", encoding="utf-8") as f:
        raw_data = f.read()
        # Trim a trailing separator if present to avoid an empty final pair
        if raw_data.endswith("{-line_break-}"):
            raw_data = raw_data[: -len("{-line_break-}")]
except FileNotFoundError:
    print(f"Error: Quizlet export file '{quizlet_export_file}' not found.")
    raw_data = ""


def format_test_data(raw_data):
    pairs = raw_data.split("{-line_break-}")
    formatted_test_data = []
    for pair in pairs:
        if "{-tab-}" in pair:
            term, definition = pair.split("{-tab-}")
            formatted_test_data.append({"term": term, "definition": definition})
    return formatted_test_data


def select_random_items(
    candidates: List,
    count: int,
    exclude_indices: Optional[Set[int]] = None,
) -> List[int]:
    """Select a count of random indices, excluding any provided positions."""
    exclude_indices = exclude_indices or set()
    available_count = len(candidates) - len(exclude_indices)
    if count > available_count:
        raise ValueError(
            f"Requested count ({count}) exceeds available items ({available_count})"
        )

    weights = [0 if i in exclude_indices else 1 for i in range(len(candidates))]
    selected_items = random.choices(range(len(candidates)), weights=weights, k=count)

    return selected_items


def get_question_and_answers(formatted_test_data, exclude: Optional[Set[int]] = None):
    """Build a question with one correct answer and three distractors."""
    exclude = exclude or set()
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
    """Present a question to the user, collect their answer, and report correctness.

    Args:
        question (str): The question to be asked.
        correct_answer (str): The correct answer text.
        answers (dict): Mapping of option letters to answer text.
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
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\033[92mTest administered on {timestamp}\033[0m")

    while len(asked_questions) < num_questions:
        (
            question,
            correct_answer,
            answers,
            question_index,
        ) = get_question_and_answers(
            formatted_test_data,
            exclude=asked_questions,
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
    score_line = f"Score: {num_correct}/{num_questions} ({percent_correct:.2f}%)"
    print(f"\033[92m{score_line}\033[0m")
    if incorrect_questions:
        print(f"Incorrect Questions: {', '.join(map(str, incorrect_questions))}")
    return percent_correct


if __name__ == "__main__":
    administer_test(format_test_data(raw_data))
