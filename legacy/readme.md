# 구버전 : 이 파일은 이전 버전의 소스코드입니다.
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
3. 다음의 두 가지 방법을 통한 실행파일(.exe) 생성:
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
