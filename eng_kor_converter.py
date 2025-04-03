from hangul_utils import join_jamos
# from key_map.py (legacy)
# 자음-초성/종성
CONS = {
    'r': 'ㄱ', 'R': 'ㄲ', 's': 'ㄴ', 'e': 'ㄷ', 'E': 'ㄸ',
    'f': 'ㄹ', 'a': 'ㅁ', 'q': 'ㅂ', 'Q': 'ㅃ', 't': 'ㅅ',
    'T': 'ㅆ', 'd': 'ㅇ', 'w': 'ㅈ', 'W': 'ㅉ', 'c': 'ㅊ',
    'z': 'ㅋ', 'x': 'ㅌ', 'v': 'ㅍ', 'g': 'ㅎ'
}

# 모음-중성
VOWS = {
    'k': 'ㅏ', 'o': 'ㅐ', 'i': 'ㅑ', 'O': 'ㅒ', 'j': 'ㅓ',
    'p': 'ㅔ', 'u': 'ㅕ', 'P': 'ㅖ', 'h': 'ㅗ', 'hk': 'ㅘ',
    'ho': 'ㅙ', 'hl': 'ㅚ', 'y': 'ㅛ', 'n': 'ㅜ', 'nj': 'ㅝ',
    'np': 'ㅞ', 'nl': 'ㅟ', 'b': 'ㅠ', 'm': 'ㅡ', 'ml': 'ㅢ',
    'l': 'ㅣ'
}

# 자음-종성
CONS_DOUBLE = {
    'rt': 'ㄳ', 'sw': 'ㄵ', 'sg': 'ㄶ', 'fr': 'ㄺ', 'fa': 'ㄻ',
    'fq': 'ㄼ', 'ft': 'ㄽ', 'fx': 'ㄾ', 'fv': 'ㄿ', 'fg': 'ㅀ',
    'qt': 'ㅄ'
}
# 쌍자음
SHIFT_KEYS = {'R', 'E', 'Q', 'T', 'W', 'O', 'P'}
# =============================================================================
# caller must check if len(text) == 0
def engkor(text, collapse = False): # if collapse: return str
    result = []   # 영 > 한 변환 결과
    
    # 1. 해당 글자가 자음인지 모음인지 확인
    vc_list = []
    for t in text:
        if t in CONS:
            vc_list.append('c')
        elif t in VOWS:
            vc_list.append('v')
        else:
            vc_list.append('!')
    vc = ''.join(vc_list)
    # cvv → fVV / cv → fv / cc → CC
    vc = vc.replace('cv', 'fv').replace('vv', 'VV').replace('cc', 'CC')
    
    # 2. 자음 / 모음 / 두글자 자음 에서 검색
    i = 0
    len_text = len(text)
    last_t = text[len_text - 1]
    before_last_t = text[len_text - 2]
    while i < len_text:
        v, t = vc[i], text[i]
        if v in ('f', 'c'):
            result.append(CONS[t])
        elif v == 'V':
            double_vowel = VOWS.get(text[i:i+2])
            if double_vowel:
                result.append(double_vowel)
                i += 1
            else: result.append(VOWS[t])
        elif v == 'v':
            result.append(VOWS[t])
        elif v == 'C':
            double_cons = CONS_DOUBLE.get(text[i:i+2])
            if double_cons:
                result.append(double_cons)
                i += 1
            else: result.append(CONS[t])
        else: result.append(t)
        i += 1

    result_1 = ''
    result_2 = join_jamos(''.join(result))
    split_index = 0
    if collapse: return result_2
    elif len(result_2) == 2:
        result_1 = result_2[0]
        result_2 = result_2[1]
        split_index = len_text - 1
        if last_t in VOWS and before_last_t in CONS:
            split_index -= 1

    return result_1, result_2, split_index
