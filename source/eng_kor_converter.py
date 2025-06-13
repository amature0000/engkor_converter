from hangul_utils import convert_key

# 자음
CONS = {
    'r': 'ㄱ', 'R': 'ㄲ', 's': 'ㄴ', 'e': 'ㄷ', 'E': 'ㄸ',
    'f': 'ㄹ', 'a': 'ㅁ', 'q': 'ㅂ', 'Q': 'ㅃ', 't': 'ㅅ',
    'T': 'ㅆ', 'd': 'ㅇ', 'w': 'ㅈ', 'W': 'ㅉ', 'c': 'ㅊ',
    'z': 'ㅋ', 'x': 'ㅌ', 'v': 'ㅍ', 'g': 'ㅎ'
}

# 모음
VOWS = {
    'k': 'ㅏ', 'o': 'ㅐ', 'i': 'ㅑ', 'O': 'ㅒ', 'j': 'ㅓ',
    'p': 'ㅔ', 'u': 'ㅕ', 'P': 'ㅖ', 'h': 'ㅗ', 'hk': 'ㅘ',
    'ho': 'ㅙ', 'hl': 'ㅚ', 'y': 'ㅛ', 'n': 'ㅜ', 'nj': 'ㅝ',
    'np': 'ㅞ', 'nl': 'ㅟ', 'b': 'ㅠ', 'm': 'ㅡ', 'ml': 'ㅢ',
    'l': 'ㅣ'
}

# =============================================================================
# caller must check if len(text) == 0
def engkor(text):
    result_1 = ''
    result_2 = convert_key(''.join(text), 'ko')
    split_index = 0

    len_text = len(text)
    last_t = text[len_text - 1]
    before_last_t = text[len_text - 2]

    # 현재 cursor가 2글자를 담고 있다면 -> 앞 글자를 제거
    if len(result_2) == 2:
        result_1 = result_2[0]
        result_2 = result_2[1]
        split_index = len_text - 1
        # 뒤 글자가 초성-중성 결합이라면 -> 제거하는 범위--
        if last_t in VOWS and before_last_t in CONS:
            split_index -= 1
    # '', text, 0
    return result_1, result_2, split_index
