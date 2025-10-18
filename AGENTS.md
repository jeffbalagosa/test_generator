# Repository Guidelines

## Project Structure & Module Organization
- `main.py` - interactive quiz generator handling question selection, scoring, and prompts.
- `tests/` - pytest modules (`test_*.py`) validating parsing utilities and quiz logic.
- `.vscode/` and `test_generator.code-workspace` - editor settings enforcing Black formatting and format-on-save.
- `pyproject.toml`, `.flake8`, `.gitignore`, `requirements-dev.txt` - tool configuration and developer dependencies.

## Build, Test, and Development Commands
- `.\.venv\Scripts\activate` - PowerShell activation of the local virtualenv.
- `python main.py` - run the quiz; press `Ctrl+C` to exit early.
- `pytest` - execute automated tests; add `-k <name>` for targeted runs.
- `flake8` - lint for style violations and likely bugs.
- `black .` - format source files to the project standard.

## Coding Style & Naming Conventions
- Python 3.11, 4-space indentation, UTF-8 source files.
- Black controls layout (88-char lines); run before committing.
- Use `snake_case` for functions and variables, `UPPER_SNAKE_CASE` for constants, and `PascalCase` for future classes.
- Avoid mutable default arguments; prefer explicit type hints imported from `typing`.

## Testing Guidelines
- Place new tests in `tests/test_<feature>.py`; keep names descriptive.
- Patch `socket.create_connection` in tests when asserting offline behavior.
- Add regression tests whenever fixing bugs; run `pytest` until it passes without warnings.
- Aim for high coverage on new modules and ensure random operations are deterministic via seeding where needed.

## Commit & Pull Request Guidelines
- Write imperative commit subjects (`Fix empty quiz guard`); keep bodies short and focused.
- Separate formatting-only commits to simplify reviews.
- Pull requests must describe behavior changes, list test commands executed, and reference related issues.
- Confirm `flake8` and `black --check .` succeed before requesting review.

## Security & Configuration Tips
- Keep secrets and API keys out of version control; rely on `.env` files excluded by `.gitignore`.
- If outbound network checks are restricted, adjust `check_internet_connection` accordingly and document overrides in PR notes.
- Periodically refresh the virtualenv (`pip install -U -r requirements-dev.txt`) to receive linting updates.
