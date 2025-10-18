import random
from unittest.mock import patch, MagicMock
import pytest

from main import (
    format_test_data,
    select_random_items,
    get_question_and_answers,
    check_internet_connection,
    prompt_user_question,
)


class TestFormatTestData:
    def test_format_test_data_basic(self):
        raw_data = "term1{-tab-}def1{-line_break-}term2{-tab-}def2"
        expected = [
            {"term": "term1", "definition": "def1"},
            {"term": "term2", "definition": "def2"},
        ]
        assert format_test_data(raw_data) == expected

    def test_format_test_data_empty(self):
        assert format_test_data("") == []

    def test_format_test_data_no_separator(self):
        raw_data = "term1{-tab-}def1"
        expected = [{"term": "term1", "definition": "def1"}]
        assert format_test_data(raw_data) == expected

    def test_format_test_data_trailing_separator(self):
        raw_data = "term1{-tab-}def1{-line_break-}"
        expected = [{"term": "term1", "definition": "def1"}]
        assert format_test_data(raw_data) == expected


class TestSelectRandomItems:
    def test_select_random_items_basic(self):
        random.seed(42)  # For deterministic test
        candidates = [1, 2, 3, 4, 5]
        result = select_random_items(candidates, 3)
        assert len(result) == 3
        assert all(idx in range(len(candidates)) for idx in result)

    def test_select_random_items_with_exclude(self):
        random.seed(42)
        candidates = [1, 2, 3, 4, 5]
        exclude = {0, 2}
        result = select_random_items(candidates, 2, exclude)
        assert len(result) == 2
        assert all(idx not in exclude for idx in result)

    def test_select_random_items_count_too_large(self):
        candidates = [1, 2, 3]
        with pytest.raises(ValueError):
            select_random_items(candidates, 5)

    def test_select_random_items_exclude_all(self):
        candidates = [1, 2, 3]
        exclude = {0, 1, 2}
        with pytest.raises(ValueError):
            select_random_items(candidates, 1, exclude)


class TestGetQuestionAndAnswers:
    def test_get_question_and_answers_basic(self):
        random.seed(42)
        test_data = [
            {"term": "Q1", "definition": "A1"},
            {"term": "Q2", "definition": "A2"},
            {"term": "Q3", "definition": "A3"},
            {"term": "Q4", "definition": "A4"},
            {"term": "Q5", "definition": "A5"},
        ]
        question, correct, answers, q_idx = get_question_and_answers(test_data)
        assert question in [item["term"] for item in test_data]
        assert correct in [item["definition"] for item in test_data]
        assert len(answers) == 4  # A, B, C, D
        assert correct in answers.values()

    def test_get_question_and_answers_with_exclude(self):
        random.seed(42)
        test_data = [
            {"term": "Q1", "definition": "A1"},
            {"term": "Q2", "definition": "A2"},
            {"term": "Q3", "definition": "A3"},
            {"term": "Q4", "definition": "A4"},
            {"term": "Q5", "definition": "A5"},
            {"term": "Q6", "definition": "A6"},
        ]
        exclude = {0}
        question, correct, answers, q_idx = get_question_and_answers(test_data, exclude)
        assert q_idx != 0  # Should not select excluded index
        assert question in [item["term"] for item in test_data]
        assert correct in [item["definition"] for item in test_data]


class TestCheckInternetConnection:
    @patch("socket.create_connection")
    def test_check_internet_connection_success(self, mock_create):
        mock_create.return_value = MagicMock()
        assert check_internet_connection() is True

    @patch("socket.create_connection")
    def test_check_internet_connection_failure(self, mock_create):
        mock_create.side_effect = OSError
        assert check_internet_connection() is False


class TestPromptUserQuestion:
    @patch("builtins.input")
    @patch("main.check_internet_connection")
    @patch("builtins.print")
    def test_prompt_user_question_correct(self, mock_print, mock_check, mock_input):
        mock_input.return_value = "A"
        mock_check.return_value = False
        answers = {"A": "correct", "B": "wrong1", "C": "wrong2", "D": "wrong3"}
        result = prompt_user_question("Test question", "correct", answers)
        assert result is True

    @patch("builtins.input")
    @patch("main.check_internet_connection")
    @patch("builtins.print")
    def test_prompt_user_question_incorrect(self, mock_print, mock_check, mock_input):
        mock_input.return_value = "B"
        mock_check.return_value = False
        answers = {"A": "correct", "B": "wrong1", "C": "wrong2", "D": "wrong3"}
        result = prompt_user_question("Test question", "correct", answers)
        assert result is False

    @patch("builtins.input")
    @patch("main.check_internet_connection")
    @patch("builtins.print")
    def test_prompt_user_question_invalid_input(
        self, mock_print, mock_check, mock_input
    ):
        mock_input.side_effect = ["X", "A"]
        mock_check.return_value = False
        answers = {"A": "correct", "B": "wrong1", "C": "wrong2", "D": "wrong3"}
        result = prompt_user_question("Test question", "correct", answers)
        assert result is True
