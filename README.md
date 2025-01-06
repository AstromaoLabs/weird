# **Weird**

## **Overview**
Weird is a Python-based command-line tool designed to convert markdown and code files into static websites. The generated websites preserve the formatting of markdown while adding features like syntax highlighting, easy navigation, and downloadable code snippets. The goal is to provide a user-friendly, out-of-the-box solution that requires minimal setup as long as Python is installed, Weird tries to handle the rest.

With Weird, users can write markdown, run a single command, and have a functional, deployable static site.

---

## **Features**

_As this project is still under early development, certain features may contain bugs or not be implemented._

### **Markdown Conversion**
- Converts markdown files into HTML with proper formatting and styling.
- Supports common markdown syntax like headings, lists, and inline formatting.

### **Syntax Highlighting**
- Highlights code blocks in multiple languages for readability.

### **Navigation**
- Generates a fully navigable website when provided with a directory of markdown files.
- Automatically links pages and creates an index or navigation bar.

### **Code Snippet Management**
- Allows code segments to be downloaded directly from the website.
- (Could possibly support inline code execution on specific pages. Not yet decided)

### **Custom Configuration**
- Uses a JSON configuration file to customize themes, colors, and metadata (e.g., site name, descriptions).  (Not yet decided)
- Allows users to include custom CSS files for additional styling. ( Not yet decided)

### **Deployment Ready**
- Builds static websites that can be deployed to GitHub Pages or other hosting platforms.
- Includes options for automatic GitHub Pages deployment.

### **Local and Offline Support**
- Websites can be run locally without requiring external tools or internet connectivity.

---

## **Setup and Usage**

### **Prerequisites**
- Python 3.8+

### **Installation**  
```bash
pip install weird
```

### **Basic Usage**
To convert a directory of markdown files into a website:
```bash
python -m weird build <input-directory> <output-directory>
```

### **Configuration**
To customize your website:
1. Run the ``configure`` command.
   ```bash
   python -m weird configure
   ```

   This will create the `weird_config.json` file in your current directory, with all configuration options set at their defaults.

   Alternatively, create the `weird_config.json` file manually in your project directory.

2. Add/modify configuration options:
   ```json
   {
       "site_name": "My Cool Website",
       "theme": "dark",
       "custom_css": "styles/custom.css"
   }
   ```
3. Weird will apply these settings during the build next process.

---

## **Technology Stack**

### **Build System**
- **Python**: Processes markdown files and generates HTML/CSS/JS for static sites.

### **Frontend**
- **Vanilla HTML/CSS/JS**: Ensures compatibility with GitHub Pages and avoids the need for additional frameworks.

---

## **Development Roadmap**

### **Planned Features**
1. **Advanced Themes**: Pre-built themes with customizable options. (Not yet decided)
2. **Interactive Code Blocks**: Enable code execution in-browser for supported languages. (Not yet decided)
3. **Dynamic Search**: Add a search bar to navigate large sites. (Not yet decided)
4. **Preview Command**: Add a local preview mode to test sites before deployment. (Not yet decided)

### **Collaborator Notes**
- Keep the CLI as user-friendly as possible while supporting advanced configurations.
- Avoid adding dependencies unless absolutely necessary to maintain simplicity.

---

## **Contributing**
To contribute:
1. Follow the guide found at [CONTRIBUTING.md](CONTRIBUTING.md).

Key principles:
- Use feature branches for all development.
- Write clear, descriptive commit messages.
- Test thoroughly before submitting pull requests.

---

## **License**
Weird is currently not licensed. For inquiries about usage or contributions, please contact the maintainers.

---

### **Notes**
- Ensure sensitive data (e.g., API keys, credentials) is never committed to the repository.
- Refer to the [Issues page](https://github.com/AstromaoLabs/weird/issues) for open tasks.
- This project is a work in progress, and we welcome feedback and suggestions!