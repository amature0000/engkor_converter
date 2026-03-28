from hangul_utils import convert_key

# 자음
CONS = {
    'r', 'R', 's', 'e', 'E',
    'f', 'a', 'q', 'Q', 't',
    'T', 'd', 'w', 'W', 'c',
    'z', 'x', 'v', 'g'
}

# 모음
VOWS = {
    'k', 'o', 'i', 'O', 'j',
    'p', 'u', 'P', 'h', 'hk',
    'ho', 'hl', 'y', 'n', 'nj',
    'np', 'nl', 'b', 'm', 'ml',
    'l'
}

def engkor(text):
    result = convert_key(''.join(text), 'ko')
    split_index = 0

    if len(result) == 2:
        split_index = len(text) - 1
        # 마지막 2 글자가 초성-중성 조합인 경우
        if text[-1] in VOWS and text[-2] in CONS:
            split_index -= 1
            
    return result, split_index
