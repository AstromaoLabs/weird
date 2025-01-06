# **Contributing to Weird**

Thank you for considering contributing to this project! Please follow these guidelines to ensure a smooth and productive workflow for everyone.

---

## **Getting Started**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AstromaoLabs/weird
   cd weird
   ```
2. **Setup a virtual environment:**

   If you are using bash:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   If you are on windows the path is `.venv/Scripts/activate` instead.
   If you are working in cmd/powershell you do not use the `source` command.:
   ```bash
   python -m venv .venv
   .venv/Scripts/activate
   ```

3. **Install dependancies**

   While in your virtual environment, install dependancies:
   ```bash
   pip install -r requirements.txt
   ```

4. **Follow the workflow in the section below**:

---

## **Workflow**

1. **Pick or create an issue**:
   
   When picking an existing issue:
   - Browse the [GitHub Issues](https://github.com/AstromaoLabs/weird/issues) for tasks.
   - Comment on the issue to indicate you're working on it.
   
   When creating an issue:
   - Identify what you would like to work on.
   - Visit our [Github Issues](https://github.com/AstromaoLabs/weird/issues) and check if this issue is already open.
   - [Create Your Issue](https://github.com/AstromaoLabs/weird/issues/new) if it is not a duplicate.
   
   You can find our issue template [here](./.github/issue_template.md).

2. **Create a fork of the repository**:

   You can view github's documentation on forks [here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)

3. **Create a new branch for your work**:
   - Use the following naming format:
     ```bash
     git switch -c issue-#<issue-number>-<short-description>
     ```
     Example:
     ```bash
     git switch -c issue-#3-add-file-generation
     ```
     
4. **Work on your branch**:
   - Implement your changes.
   - Make small, meaningful commits:
     ```bash
     git add <file>
     git commit -m "<issue-type>: <message>; addresses #<issue-number>"
     ```
     Example:
     ```bash
     git add CONTRIBUTING.md
     git commit -m "docs: Add contribution guidelines for project; resolves #3"
     ```

5. **Push your branch**:
   ```bash
   git push origin issue-#<issue-number>-<short-description>
   ```

---

## **Create a Pull Request (PR)**

1. Open a new PR on GitHub. The PR should be from your fork's branch for the issue to the reposity's `main` branch.
2. Fill out the required details in the PR template (this will appear automatically).
3. Link the PR to the issue by including `Fixes #<issue-number>` or `Resolves #<issue-number>`in the description or one of the commit messages.
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

If you have any questions, feel free to comment under the relevant issue, open a new one, or contact us on [Github Discussions](https://github.com/AstromaoLabs/weird/discussions).

---

Thank you for contributing!