# weird
WIP: A python tool for converting markdown into websites

## concept

This project will be a terminal-based tool for converting markdown and code files into websites.

These websites will essentially display the markdown/code, but including all the benefits of a markdown engine/syntax highlighting.

To use it should be as simple as:
```bash
python -m weird build <input-directory> <output-directory>
```
There might be other configuration options as well but this is the basic idea.

From the build website the user should be able to navigate easily, as well as be able to either run code from the website, download segments of code, or navigate to a page where they can test-run code.
The website should be able to run locally without the user having to download lots of external tools, and should be able to be deployed onto github pages.

## technologies

There are two parts currently in mind for this project.

**1.** The system to build the website.
**2.** The built website.

For **1.**, since we are really building html files and processing user input, python itself should be fine.

For **2.**, to prevent the user from having to download any frameworks or anything and to make sure it works on github pages, I would like to stick with vanilla html/css/js if possible.