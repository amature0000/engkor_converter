[![GitHub downloads](https://img.shields.io/github/downloads/amature0000/engkor_converter/total.svg?logo=github)](https://github.com/amature0000/engkor_converter/releases)
# 영-한 문자열 변환 프로그램
## 소개
이 프로그램은 IME를 지원하지 않는 채팅창에서 한글을 출력하기 위해 개발되었습니다.

이 프로그램은 키보드 훅을 이용해 사용자 입력을 가로채고 가상 키보드를 활용해 한글 채팅 출력을 시뮬레이션합니다.

## 프로젝트 구조
```
runme.py
    ├─ Logger: 프로그램 실행 정보 및 채팅창 상태를 실시간으로 출력하는 클래스
    │     • @log_typing: 클래스 외부 데코레이터로 EventHandler 메소드에 사용되어야 함.
    │
    ├─ EventHandler: os 레벨의 키보드 이벤트를 받아 처리하는 클래스
    │     • process(): 키보드 이벤트를 받아 상태를 업데이트하고 State 객체로 전달
    │
    └─ State: 한글 IME 기능 및 가상 입력을 수행하는 클래스
          • _record(): 키보드 이벤트를 누적
          • _update_state(): 누적된 키보드 입력을 바탕으로 출력할 텍스트 계산
          • _calculate_diff(): 출력할 텍스트와 직전 텍스트를 비교하여 가상 키보드가 수행할 입력 계산
          • process(): 가상 키보드 입력을 통해 계산된 텍스트 출력
```

## related work
- [한글 키보드 입력 변환](https://mizykk.tistory.com/115)
- [hangul-bypass](https://github.com/chyangpa/hangul-bypass)