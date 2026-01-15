[![GitHub downloads](https://img.shields.io/github/downloads/amature0000/engkor_converter/total.svg?logo=github)](https://github.com/amature0000/engkor_converter/releases)
# 영-한 문자열 변환 프로그램
## 소개
### [사용법](https://reinvented-oak-967.notion.site/EK-converter-2e54a4ebe77b80859899e066f14a411a)
이 프로그램은 HELLDIVERS™ 2 인게임 채팅에 활용됩니다. 키보드 입력을 모니터링하고, 인게임 채팅창을 대체하여 **한글 채팅**을 지원하는 채팅창을 디스플레이합니다.

소스코드를 수정하여 다른 게임에 응용할 수 있습니다.

## for modification
소스코드를 수정해 다른 게임에 적용하는 예시입니다.

- `utils.py`: `game_title`을 원하는 게임명으로 변경
```python
# utils.py

def get_window_rect():
    game_title = "HELLDIVERS™ 2"
    global get_window_rect
    get_window_rect = None
    ...
```

- `overlay.py`:
    - `*_R`들을 이용해 채팅창의 크기 설정
    - `offset_*`들을 이용해 채팅창의 위치 설정
```python
# overlay.py

# ratio
WIDTH_R = 18.75 #470
HEIGHT_R = 3.9 #50
...

        # logistic regression
        offset_x = -22.90 * hud_size + 99.93
        offset_y = -12.50 * hud_size + 99.78
```

소스코드 위치는 바탕화면의 `EKconverter` 우클릭 - 파일 위치 열기 - 상위 폴더(EKconverter)로 이동 후 source 폴더로 이동

## related work
- [한글 키보드 입력 변환](https://mizykk.tistory.com/115)
- [embeddable pakage에서 tkinter 사용](https://www.sysnet.pe.kr/2/0/13922?pageno=3)
- [helldivers2_helper](https://github.com/rubystarashe/helldivers2_helper)
- [dead_by_unicode_gui](https://github.com/Codex-in-somnio/dead_by_unicode_gui)
