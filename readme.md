# 영-한 문자열 변환 프로그램 v3
## 소개
이 프로그램은 Python 기반의 실행프로그램입니다. 키보드 입력을 모니터링하고, 모니터링된 **알파벳**을 조합하여 **한글 문장**으로 대체합니다.

이 프로그램은 HELLDIVERS™ 2 인게임 채팅에 활용됩니다. 소스코드를 수정하여 다른 게임에 응용할 수 있습니다.

## 소스코드 및 다운로드
- Python 3.10 (권장)
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

### 다운로드
[릴리즈 보러 가기]()
### 주의: 몇몇 보안 프로그램에서 download.zip 파일을 바이러스로 탐지합니다. 이는 오탐지이며, 대신 직접 소스코드 설치를 통해 실행파일을 생성할 수 있습니다.

## 레퍼런스
- [(tistory)한글 키보드 입력 변환하기](https://mizykk.tistory.com/115) 에 게시된 eng-kor 변환 파이썬 코드를 사용합니다.
- [helldivers2_helper](https://github.com/rubystarashe/helldivers2_helper) 프로젝트 및 [dead_by_unicode_gui](https://github.com/Codex-in-somnio/dead_by_unicode_gui) 프로젝트로부터 한글화 아이디어를 차용했습니다.

<hr>

## 동작화면

![img](for_readme/1.png)
![img](for_readme/2.png)
![img](for_readme/3.png)
![img](for_readme/4.png)