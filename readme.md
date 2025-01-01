# ENG - KOR converter program
![gifs](for_readme/Animation.webp)
![gifs](for_readme/Animation2.webp)
## Introduction
This program is a Python-based application. It monitors your keyboard input, converts&assembles it into **Korean string**, and replaces the original **English string**.

This program is dedicated for in-game chatting, which opens the chat box with the `enter` key. You can modify source code for other uses.

## Dependencies and Installation
- Python >= 3.10
### Installation
1. clone repo
    ```
    git clone https://github.com/amature0000/engkor_converter.git
    ```
2. Install dependent packages
    ```
    pip install -r requirements.txt
    ```
3. There are 2 ways to create an excutable(.exe) file:
    ```
    pyinstaller --onefile --icon=favicon.ico runme.py
    ```
    ```
    nuitka --onefile --standalone --follow-imports --windows-icon-from-ico=favicon.ico runme.py
    ```

### Download
[download.zip](https://github.com/amature0000/engkor_converter/releases)

## Reference
I used the Eng-Kor converter code from this [blog post](https://mizykk.tistory.com/115). Please refer to it for more details.
