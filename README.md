I’ve built a scalable, hybrid automation framework from scratch using Playwright, Pytest, and GitHub Actions. It supports web, API, and DB testing, is resolution-aware, and is designed for CI/CD execution with clean reporting and modular design.

#Install the dependencies:
pip install -r requirements.txt

#And install Playwright browsers:
playwright install

# Running Tests Locally
- By default, tests run in headless mode.
- To run tests in headed mode for debugging, use the `--headed` option:
  ```bash
  pytest --headed

# CI/CD Execution
- Tests are executed in headless mode by default in the CI/CD pipeline for faster execution.
- The HEADLESS environment variable is set to true in the GitHub Actions workflow.
