import random


raw_data = """Who was the author of the problem-solving approach discussed in the first chapter?{-tab-}Charles{-line_break-}Which company did Charles intern at in Japan?{-tab-}Canon{-line_break-}What was Charles' seemingly impossible task during his internship at Canon?{-tab-}Develop a model for how to site factories{-line_break-}What did Charles use to capture the variables and their impacts in his model?{-tab-}A logic tree{-line_break-}What is the core focus of the book?{-tab-}The decision-making power of simple logical structures and processes in problem solving{-line_break-}What does problem solving mean according to the book?{-tab-}Making better decisions on complicated challenges of personal life, workplaces, and the policy sphere{-line_break-}How many steps are in the Bulletproof Problem Solving Process?{-tab-}Seven{-line_break-}What visual tool is emphasized for disaggregating problems?{-tab-}Logic trees{-line_break-}What are the three main aspects evaluated in the Sydney Airport case study?{-tab-}Supply, demand, and runway utilization{-line_break-}What are the criteria Rob used to decide whether to install solar panels?{-tab-}Payback period, decline in cost of panels, and reduction in CO2 footprint{-line_break-}What approach did Charles use to decide where to move with his family?{-tab-}Breaking down the problem into measurable indicators and applying weights{-line_break-}What kind of tree did Charles use for the start-up company's pricing decision?{-tab-}Profit lever tree{-line_break-}How does the book suggest dealing with the elevator test situation?{-tab-}Have a coherent summary of the problem and solution path at any point in the project{-line_break-}What is the key problem identified in US K-12 education according to Charles' research?{-tab-}Teacher characteristics and the school environment{-line_break-}What is the significance of logic trees in problem solving according to the book?{-tab-}They provide a clear visual representation, capture everything relevant, and lead to clear hypotheses that can be tested with data and analysis{-line_break-}"""


def format_test_data(raw_data):
    """
    Formats raw test data containing terms and definitions separated by
    special markers into a list of dictionaries.

    Parameters:
    - raw_data (str): A string containing terms and their definitions,
    separated by "{-tab-}" and "{-line_break-}".

    Returns:
    - list: A list of dictionaries, where each dictionary has 'term' and
    'definition' keys.
    """

    pairs = raw_data.split("{-line_break-}")

    formatted_test_data = []

    for pair in pairs:
        if "{-tab-}" in pair:
            term, definition = pair.split("{-tab-}")
            formatted_test_data.append({"term": term, "definition": definition})

    return formatted_test_data


# Get one random question and its answer, plus 3 random wrong answers from the formatted test data
def get_question_and_answers(formatted_test_data):
    """
    Gets one random question and its answer, plus 3 random wrong answers
    from the formatted test data.

    Parameters:
    - formatted_test_data (list): A list of dictionaries, where each
    dictionary has 'term' and 'definition' keys.

    Returns:
    - tuple: A tuple containing the question (str), the correct answer (str),
    and a list of 3 wrong answers (list of str).
    """

    question_data = random.choice(formatted_test_data)
    correct_answer = question_data["definition"]

    wrong_answers = []

    while len(wrong_answers) < 3:
        random_answer = random.choice(formatted_test_data)["definition"]
        if random_answer != correct_answer and random_answer not in wrong_answers:
            wrong_answers.append(random_answer)

    answers = [correct_answer] + wrong_answers
    random.shuffle(answers)

    return question_data["term"], correct_answer, answers


def prompt_user(question, correct_answer, answers):
    """
    Prompts the user with a multiple-choice question and checks if the
    answer is correct.

    Parameters:
    - question (str): The question to ask the user.
    - correct_answer (str): The correct answer to the question.
    - answers (list): A list of answer options (including the correct answer).

    Returns:
    - bool: True if the user's answer is correct, False otherwise.
    """

    print(question)

    for i, answer in enumerate(answers, 1):
        print(f"{i}. {answer}")

    user_answer = input("Enter the number of your answer: ")

    if answers[int(user_answer) - 1] == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"Wrong! The correct answer is: {correct_answer}")
        return False


formatted_test_data = format_test_data(raw_data)
question, correct_answer, answers = get_question_and_answers(formatted_test_data)
prompt_user(question, correct_answer, answers)
