# 영-한 문자열 변환 프로그램 v3
## 소개
이 프로그램은 Python 기반의 실행프로그램입니다. 키보드 입력을 모니터링하고, 인게임 채팅창을 대체하여 **한글 채팅**을 지원하는 채팅창을 디스플레이합니다.

이 프로그램은 HELLDIVERS™ 2 인게임 채팅에 활용됩니다. 소스코드를 수정하여 다른 게임에 응용할 수 있습니다.

## 소스코드 및 다운로드
- Python 3.10 (권장)
### 소스코드 설치
1. 레포지토리 클론
    ```
    git clone https://github.com/amature0000/engkor_converter.git
    ```
2. 해당 디렉토리로 이동 후 요구 패키지 설치
    ```
    pip install -r requirements.txt
    ```
3. 실행파일(.exe) 생성:
    ```
    pyinstaller --icon=favicon.ico runme.py
    ```
    

### 다운로드
[릴리즈 보러 가기](https://github.com/amature0000/engkor_converter/releases)
### 주의: 몇몇 보안 프로그램에서 다운로드 파일을 바이러스로 탐지합니다. 이는 오탐지이며, 직접 소스코드 설치를 통해 실행파일을 생성할 수 있습니다.

## related work
- [helldivers2_helper](https://github.com/rubystarashe/helldivers2_helper): 한글 채팅을 포함해 다양한 기능을 지원하는 헬다이버즈2 매니저 프로그램
- [dead_by_unicode_gui](https://github.com/Codex-in-somnio/dead_by_unicode_gui): 가상 키보드를 활용해 사용자 입력을 모니터링하고 출력하는 프로그램

## 버전
### ver 3(3.xx)
화면 위로 오버레이 창을 띄워, 기존 채팅창을 가리고 사용자 키보드 입력을 모니터링
### ver 4(4.xx)
화면 위로 새로운 입력 창을 띄워, 커서 포커스를 해당 입력창으로 이동시키고 사용자 입력을 받아옴
