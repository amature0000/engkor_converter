# ENG - KOR converter program
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
### NOTE: Some antivirus vendors detect this file as malware. It is a false detection, but if you don't want to risk it, create the .exe file yourself via the Installation method above.

## Reference
I used the Eng-Kor converter code from this [blog post](https://mizykk.tistory.com/115). Please refer to it for more details.

<hr>

# 영-한 문자열 변환 프로그램
## 소개
이 프로그램은 Python 기반의 실행프로그램입니다. 키보드 입력을 모니터링하고, 모니터링된 **알파벳**을 조합하여 **한글 문장**으로 대체합니다.

이 프로그램은 `enter` 키로 채팅창을 열고 닫는 인게임 채팅에 활용됩니다. 소스코드를 수정하여 동작을 변경할 수 있습니다.

## 소스코드 및 다운로드
- Python >= 3.10
### 소스코드 설치
1. 레포지토리 클론
    ```
    git clone https://github.com/amature0000/engkor_converter.git
    ```
2. 요구 패키지 설치
    ```
    pip install -r requirements.txt
    ```
3. 다음의 두 가지 방법을 실행파일(.exe) 생성:
    ```
    pyinstaller --onefile --icon=favicon.ico runme.py
    ```
    ```
    nuitka --onefile --standalone --follow-imports --windows-icon-from-ico=favicon.ico runme.py
    ```

### 다운로드
[download.zip](https://github.com/amature0000/engkor_converter/releases)
### 주의: 몇몇 보안 프로그램에서 download.zip 파일을 바이러스로 탐지합니다. 이는 오탐지이지만, 불안하다면 위의 과정을 통해 수동으로 .exe 파일을 생성할 수 있습니다.

## 레퍼런스
다음 [블로그 게시물](https://mizykk.tistory.com/115)로부터 eng-kor 변환 파이썬 코드를 참고했습니다.

<hr>

![gifs](for_readme/Animation.webp)
![gifs](for_readme/Animation2.webp)
