# Quizlet Test Generator

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Tests](https://img.shields.io/badge/Tests-Pytest%20✔-yellow.svg)
![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-000000.svg)

A clean, offline-friendly CLI quiz tool that transforms **Quizlet exports** into randomized multiple-choice tests. Perfect for studying, classrooms, or gamified review sessions.

---

## 🚀 Features

* **📄 Quizlet Export Parser** – Converts text files with `{-tab-}` and `{-line_break-}` markers.
* **🎲 Randomized Testing** – Shuffles both questions and answers for each run.
* **🧩 Multiple-Choice Interface** – 4-option (A–D) questions with instant validation.
* **📊 Score Summary** – Displays results and incorrect question numbers.
* **🔒 Offline Integrity Check** – Detects internet connection ("cheating" warning).
* **🧪 Pytest Coverage** – Unit tested for consistency and reliability.

---

## 📁 Project Structure

```
.
├── main.py                    # Core logic
├── quizlet_exports/
│   └── micah/12-rules.txt     # Sample Quizlet export
├── tests/
│   └── test_main.py           # Pytest test suite
├── pyproject.toml             # Tooling configuration
├── .flake8                    # Linter configuration
└── repomix.config.json        # Repo packing configuration
```

---

## 🧩 Requirements

* Python **3.11+**
* `pytest` *(optional, for testing)*

---

## ⚙️ Installation

```bash
git clone https://github.com/<your-username>/quizlet-test-generator.git
cd quizlet-test-generator
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

*(No third-party dependencies needed for core functionality.)*

---

## 🧠 Usage

1. Export your Quizlet set to `.txt` format.
2. Verify markers:

   * `{-tab-}` → separates term and definition.
   * `{-line_break-}` → separates flashcards.
3. Place file at `quizlet_exports/<your_name>/<set>.txt`.
4. Run:

```bash
python main.py
```

The app will automatically generate randomized questions and answers.

---

## 💬 Example Session

```
Test administered on 2025-10-17 21:04:02

1) What does it mean to "stand tall" in a tough situation?

A. Sit quietly and wait for help
B. Stay confident and calm, even when things are difficult
C. Avoid confrontation at all costs
D. Act before thinking

Enter the letter of your answer: B
✅ Correct!

2) Why is it important to choose good friends?

A. They support your goals and encourage positive choices
B. They tell you what to do
C. They make life more exciting
D. They help you avoid all problems

Enter the letter of your answer: A
✅ Correct!

Score: 2/2 (100.00%)
```

If the app detects an internet connection mid-test:

```
Internet connection detected. YOU ARE CHEATING!
```

---

## 🧪 Running Tests

Run unit tests with:

```bash
pytest -v
```

---

## 🧼 Code Quality

```bash
black . --line-length 88
flake8 .
```

---

## 🛡️ License

MIT License © 2025 — [Your Name]

---

## 🌟 Quick Start

```bash
git clone https://github.com/<your-username>/quizlet-test-generator.git
cd quizlet-test-generator
python main.py
```

Start quizzing instantly — offline, randomized, and distraction-free!
