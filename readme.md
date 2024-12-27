# ENG - KOR converter program
![gifs](for_readme/Animation.webp)
![gifs](for_readme/Animation2.webp)
### Introduction
This program is a Python-based application. It monitors your keyboard input, converts&assembles it into **Korean string**, and replaces the original **English string**.

This program is dedicated for in-game chatting, which opens the chat box with the `enter` key. You can modify source code for other uses.

## How to run
1. Download [`download.zip`](https://github.com/amature0000/engkor_converter/releases).
2. Place both files in the same directory and run `runme.exe` 
    - `config.json` is optional; missing config file will make program run as default settings
3. Press the `start key` to start recording your keyboard input, and press the `end key` to stop recording and print your inputs.
    - If the `start key` and `end key` are the same, it will function as a `toggle key`.
    - default settings are: `start key`: `enter, \`, `end key`: `\`
4. Press the `esc` key to reset the program.
5. You can change the operation keys editting `config.json`

## Reference
I used the Eng-Kor converter code from this [blog post](https://mizykk.tistory.com/115). Please refer to it for more details.
