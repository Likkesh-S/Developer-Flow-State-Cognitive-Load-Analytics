
# Contributing to CogniStream

## 1. Introduction

Thank you for your interest in contributing to CogniStream!

CogniStream is an educational data analytics project that explores simulated developer activity, focus indicators, interruptions, context switching, and cognitive-load indicators.

Contributions are welcome to improve the code, documentation, testing, visualizations, and overall project quality.

## 2. How to Contribute

You can contribute by:

- Improving Python scripts.
- Fixing bugs.
- Improving SQL queries.
- Adding data validation checks.
- Improving machine-learning evaluation.
- Developing dashboard features.
- Improving project documentation.
- Adding automated tests.
- Suggesting new analytical features.

## 3. Getting Started

### Step 1: Download the Repository

1. Open the CogniStream GitHub repository.
2. Click the green Code button.
3. Select Download ZIP.
4. Extract the downloaded folder.

For a Git-based workflow, clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/cognistream-developer-analytics.git
```

Replace `YOUR-USERNAME` with the actual GitHub username or organization that owns the repository.

### Step 2: Open the Project

Open the extracted or cloned project folder in Visual Studio Code or another code editor.

### Step 3: Install Dependencies

Run:

```bash
python -m pip install -r requirements.txt
```

## 4. Contribution Workflow

Follow these steps when making changes.

### Step 1: Create a Branch

```bash
git checkout -b feature/your-feature-name
```

### Step 2: Make Changes

Modify the relevant Python, SQL, test, or documentation files.

Keep changes focused on one feature or issue whenever possible.

### Step 3: Test Your Changes

Run:

```bash
python -m unittest discover -s tests -v
```

Also run any relevant project scripts to verify that the changes work.

### Step 4: Commit Your Changes

```bash
git add .
git commit -m "Describe your changes"
```

### Step 5: Push Your Branch

```bash
git push origin feature/your-feature-name
```

### Step 6: Create a Pull Request

1. Open the repository on GitHub.
2. Select your pushed branch.
3. Click Compare & pull request.
4. Explain what you changed.
5. Submit the pull request for review.

## 5. Coding Guidelines

Contributors should:

- Use clear and meaningful variable names.
- Follow consistent Python formatting.
- Write reusable functions where appropriate.
- Add comments when logic needs explanation.
- Avoid unnecessary duplicate code.
- Validate input data.
- Handle errors appropriately.
- Keep dependencies documented.
- Avoid committing passwords, API keys, or private information.

## 6. Data Guidelines

The project currently uses simulated developer activity data.

When adding or modifying datasets:

- Document every column.
- Use consistent data types.
- Check for missing and duplicate values.
- Validate numerical ranges.
- Avoid including personal or confidential information.
- Clearly identify simulated or synthetic data.

Any real-world data collection must have appropriate permissions, consent, and privacy safeguards.

## 7. Testing Guidelines

Before submitting a contribution:

1. Run the automated tests.
2. Check relevant scripts.
3. Verify generated outputs.
4. Check SQL operations if database code changed.
5. Test dashboard behavior if visualization code changed.
6. Update documentation when necessary.

Run all tests using:

```bash
python -m unittest discover -s tests -v
```

## 8. Documentation Guidelines

When adding a new feature:

- Explain its purpose.
- Document installation requirements.
- Include usage instructions.
- Describe important inputs and outputs.
- Update the README if the project overview changes.
- Update the data dictionary if dataset columns change.

## 9. Machine Learning Guidelines

Changes to the machine-learning component should:

- Explain the selected features.
- Document the target variable.
- Use an appropriate evaluation strategy.
- Report relevant metrics.
- Identify limitations.
- Avoid unsupported claims about predictive accuracy.

The current focus and cognitive-load indicators are illustrative, not clinically validated measurements.

## 10. Reporting Bugs

When reporting an issue, include:

- A short issue title.
- A description of the problem.
- Steps to reproduce the problem.
- The expected behavior.
- The actual behavior.
- Relevant error messages.
- Your Python version and operating system.

Do not include passwords, private data, or confidential records.

## 11. Feature Suggestions

Feature suggestions are welcome.

Examples include:

- Additional dashboard charts.
- Improved data validation.
- More SQL analysis queries.
- Better model evaluation.
- Automated report generation.
- Additional unit tests.
- Improved documentation.

Explain the purpose and expected benefit of the proposed feature.

## 12. Code of Conduct

All contributors are expected to:

- Communicate respectfully.
- Welcome constructive feedback.
- Avoid discriminatory or offensive behavior.
- Respect the work of other contributors.
- Protect private and confidential information.
- Focus discussions on improving the project.

## 13. License

By contributing, you agree that your contributions will be made available under the project's MIT License, subject to the terms of that license.

Refer to the root `LICENSE` file for details.

## 14. Contact and Support

For questions, suggestions, or project-related discussions, use the GitHub Issues and Pull Requests sections of the repository.

## 15. Thank You

Thank you for helping improve CogniStream!

Every useful contribution helps make the project more understandable, maintainable, and valuable as an educational data analytics project.
