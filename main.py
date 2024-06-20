import random
import socket
from datetime import datetime

# Format of the raw data: Each term (or question) and definition (or answer) pair is separated by "{-line_break-}" and the question and answer are separated by "{-tab-}" Example: "Term{-tab-}Definition{-line_break-}"
raw_data = """Who was the author of the problem-solving approach discussed in the first chapter?{-tab-}Charles{-line_break-}Which company did Charles intern at in Japan?{-tab-}Canon{-line_break-}What was Charles' seemingly impossible task during his internship at Canon?{-tab-}Develop a model for how to site factories{-line_break-}What did Charles use to capture the variables and their impacts in his model?{-tab-}A logic tree{-line_break-}What is the core focus of the book?{-tab-}The decision-making power of simple logical structures and processes in problem solving{-line_break-}What does problem solving mean according to the book?{-tab-}Making better decisions on complicated challenges of personal life, workplaces, and the policy sphere{-line_break-}How many steps are in the Bulletproof Problem Solving Process?{-tab-}Seven{-line_break-}What visual tool is emphasized for disaggregating problems?{-tab-}Logic trees{-line_break-}What are the three main aspects evaluated in the Sydney Airport case study?{-tab-}Supply, demand, and runway utilization{-line_break-}What are the criteria Rob used to decide whether to install solar panels?{-tab-}Payback period, decline in cost of panels, and reduction in CO2 footprint{-line_break-}What approach did Charles use to decide where to move with his family?{-tab-}Breaking down the problem into measurable indicators and applying weights{-line_break-}What kind of tree did Charles use for the start-up company's pricing decision?{-tab-}Profit lever tree{-line_break-}How does the book suggest dealing with the elevator test situation?{-tab-}Have a coherent summary of the problem and solution path at any point in the project{-line_break-}What is the key problem identified in US K-12 education according to Charles' research?{-tab-}Teacher characteristics and the school environment{-line_break-}What is the significance of logic trees in problem solving according to the book?{-tab-}They provide a clear visual representation, capture everything relevant, and lead to clear hypotheses that can be tested with data and analysis{-line_break-}"""


def format_test_data(raw_data):
    pairs = raw_data.split("{-line_break-}")
    formatted_test_data = []
    for pair in pairs:
        if "{-tab-}" in pair:
            term, definition = pair.split("{-tab-}")
            formatted_test_data.append({"term": term, "definition": definition})
    return formatted_test_data


def get_question_and_answers(formatted_test_data, exclude=set()):
    available_questions = [
        i for i in range(len(formatted_test_data)) if i not in exclude
    ]
    if not available_questions:
        raise ValueError("No more available questions.")
    question_index = random.choice(available_questions)
    question_data = formatted_test_data[question_index]
    correct_answer = question_data["definition"]

    wrong_answers = []
    available_wrong_answers = [
        i
        for i in range(len(formatted_test_data))
        if i != question_index and i not in exclude
    ]

    while len(wrong_answers) < 3:
        wrong_answer_index = random.choice(available_wrong_answers)
        random_answer = formatted_test_data[wrong_answer_index]["definition"]
        if random_answer not in wrong_answers:
            wrong_answers.append(random_answer)
            available_wrong_answers.remove(wrong_answer_index)

    answers = [correct_answer] + wrong_answers
    random.shuffle(answers)
    return question_data["term"], correct_answer, answers, question_index


def prompt_user_question(question, correct_answer, answers):
    print(f"{question}\n")
    for i, answer in enumerate(answers, 1):
        print(f"{i}. {answer}")
    user_answer = input("\nEnter the number of your answer: ")

    if check_internet_connection():
        print("\033[91m\nInternet connection detected. YOU ARE CHEATING!\n\033[0m")

    if answers[int(user_answer) - 1] == correct_answer:
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
    question_number = 1
    print(f"\033[92mTest administered on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\033[0m")

    while len(asked_questions) < num_questions:
        question, correct_answer, answers, question_index = get_question_and_answers(
            formatted_test_data, exclude=asked_questions
        )
        if question_index not in asked_questions:
            asked_questions.add(question_index)
            print(f"\n{question_number}) ", end="")
            if prompt_user_question(question, correct_answer, answers):
                num_correct += 1
            question_number += 1

    percent_correct = (num_correct / num_questions) * 100
    print(f"\033Score: {num_correct}/{num_questions} ({percent_correct:.2f}%)\033[0m")
    return percent_correct


administer_test(format_test_data(raw_data))
