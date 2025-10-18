# Repository Guidelines

## Project Structure & Module Organization
Keep code entry points focused in `main.py`, which drives quiz flow, question selection, and scoring. Automated validations live under `tests/`, using the `test_*.py` naming pattern so pytest auto-discovers them. Editor preferences reside in `.vscode/` and `test_generator.code-workspace`, ensuring contributors format code consistently. Tooling and dependency metadata are centralized in `pyproject.toml`, `.flake8`, `.gitignore`, and `requirements-dev.txt`.

## Build, Test, and Development Commands
Run `python main.py` after activating the virtual environment (`.\.venv\Scripts\activate`) to exercise the quiz interactively. Execute `pytest` or `pytest -k <pattern>` to validate targeted behaviors. Use `flake8` to catch style errors and potential bugs, and `black .` to reformat sources prior to committing. Refresh local tooling with `pip install -U -r requirements-dev.txt` whenever lint rules feel outdated.

## Coding Style & Naming Conventions
Target Python 3.11 with 4-space indentation in UTF-8 files. Black enforces layout (88-character lines); run it before every push to avoid CI churn. Follow `snake_case` for functions and module-level variables, reserve `UPPER_SNAKE_CASE` for constants, and prefer future classes in `PascalCase`. Avoid mutable defaults, rely on type hints from `typing`, and drop succinct comments only where logic is non-obvious.

## Testing Guidelines
Write new tests in `tests/test_<feature>.py` to stay in line with discovery rules. Use pytest fixtures and parametrization to keep cases concise. Seed random generators when verifying variable outcomes so runs stay deterministic. When mocking offline scenarios, patch `socket.create_connection` to avoid real network calls. Always ensure `pytest` passes cleanly before requesting review.

## Commit & Pull Request Guidelines
Adopt imperative commit subjects (e.g., `Fix empty quiz guard`) with focused bodies covering rationale and validation. Separate formatting-only commits from behavior changes when practical. Pull requests should outline behavior updates, enumerate validation commands (pytest, flake8, black --check), and link related issues or tickets. Highlight any deviations from default quiz flows or environment assumptions.

## Security & Configuration Tips
Keep credentials out of the repo; `.gitignore` already excludes `.env` files for local secrets. Document configuration overrides in pull requests when network restrictions or platform limitations require special handling. Periodically update the virtual environment to align with the latest linting expectations and security patches.
