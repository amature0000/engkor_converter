# ENG - KOR converter program
### Introduction
this program is a Python-based application. It monitors your keyboard input, converts&assembles to **Korean string**, and replaces the original **English string**. this program works well in the Helldivers2 game.

## How to run
1. Download [`runme.exe`](./dist/runme.exe) and [`config.json`](./dist/config.json) 
    - or you can download this [zip file](./download.zip)
2. Place both files in the same directory and run `runme.exe` 
    - `config.json` is optional; missing config file will make program run as default settings
3. Press the `start key` to start recording your keyboard input, and press the `end key` to stop recording and print your inputs.
    - If the `start key` and `end key` are the same, it will function as a `toggle key`.
4. Press the `esc` key to reset the program.
5. You can change the operation keys editting `config.json`

## Reference
I used the Eng-Kor converter code from this [blog post](https://mizykk.tistory.com/115). Please refer to it for more details.
