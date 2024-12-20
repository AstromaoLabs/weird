# **Contributing to Sightseeing Map App**

Thank you for considering contributing to this project! Please follow these guidelines to ensure a smooth and productive workflow for everyone.

---

## **Getting Started**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AstromaoLabs/weird
   cd weird
   ```
2. **Set up a virtual environment and install dependencies:**
   ```bash
   python -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

3. **Follow the workflow in the section below**:

---

## **Workflow**

1. **Pick an issue**:
   - Browse the [GitHub Issues](https://github.com/AstromaoLabs/weird/issues) for tasks.
   - Comment on the issue to indicate you're working on it.

2. **Create a new branch for your work**:
   - Use the following naming format:
     ```bash
     git checkout -b issue-#<issue-number>-<short-description>
     ```
     Example:
     ```bash
     git checkout -b issue-#3-add-file-generation
     ```
     
3. **Work on your branch**:
   - Implement your changes.
   - Make small, meaningful commits:
     ```bash
     git add .
     git commit -m "Fix #<issue-number>: <commit-message>"
     ```
     Example:
     ```bash
     git commit -m "Fix #3: Add file generation with JSON"
     ```

3. **Push your branch**:
   ```bash
   git push origin issue-#<issue-number>-<short-description>
   ```

---

## **Create a Pull Request (PR)**

1. Open a new PR on GitHub.
2. Fill out the required details in the PR template (this will appear automatically).
3. Link the PR to the issue by including `Fixes #<issue-number>` in the description.
4. Request reviewers and address any feedback.

You can find the PR template [here](.github/pull_request_template.md).

---

## **Best Practices**

- **Keep changes focused**: Address one issue per branch and PR.
- **Write meaningful commit messages**: Clearly describe your changes.
- **Test thoroughly**: Ensure all changes work as expected.
- **Follow code standards**: Adhere to the project's style and guidelines.

---

## **Need Help?**

If you have any questions, feel free to comment under the relevant issue, open a new one or contact us.

---

Thank you for contributing!