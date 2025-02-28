from hangul_utils import join_jamos
# from key_map.py (legacy)
# 자음-초성/종성
cons = {
    'r': 'ㄱ', 'R': 'ㄲ', 's': 'ㄴ', 'e': 'ㄷ', 'E': 'ㄸ',
    'f': 'ㄹ', 'a': 'ㅁ', 'q': 'ㅂ', 'Q': 'ㅃ', 't': 'ㅅ',
    'T': 'ㅆ', 'd': 'ㅇ', 'w': 'ㅈ', 'W': 'ㅉ', 'c': 'ㅊ',
    'z': 'ㅋ', 'x': 'ㅌ', 'v': 'ㅍ', 'g': 'ㅎ'
}

# 모음-중성
vowels = {
    'k': 'ㅏ', 'o': 'ㅐ', 'i': 'ㅑ', 'O': 'ㅒ', 'j': 'ㅓ',
    'p': 'ㅔ', 'u': 'ㅕ', 'P': 'ㅖ', 'h': 'ㅗ', 'hk': 'ㅘ',
    'ho': 'ㅙ', 'hl': 'ㅚ', 'y': 'ㅛ', 'n': 'ㅜ', 'nj': 'ㅝ',
    'np': 'ㅞ', 'nl': 'ㅟ', 'b': 'ㅠ', 'm': 'ㅡ', 'ml': 'ㅢ',
    'l': 'ㅣ'
}

# 자음-종성
cons_double = {
    'rt': 'ㄳ', 'sw': 'ㄵ', 'sg': 'ㄶ', 'fr': 'ㄺ', 'fa': 'ㄻ',
    'fq': 'ㄼ', 'ft': 'ㄽ', 'fx': 'ㄾ', 'fv': 'ㄿ', 'fg': 'ㅀ',
    'qt': 'ㅄ'
}

# shift keys
shift_keys = {'R', 'E', 'Q', 'T', 'W', 'O', 'P'}
# =============================================================================
# caller must check if len(text) == 0, for performance
def engkor(text, collapse = False):
    result = ''   # 영 > 한 변환 결과
    
    # 1. 해당 글자가 자음인지 모음인지 확인
    vc = '' 
    for t in text:
        if t in cons:
            vc += 'c'
        elif t in vowels:
            vc += 'v'
        else:
            vc += '!'
    
    # cvv → fVV / cv → fv / cc → CC
    vc = vc.replace('cv', 'fv').replace('vv', 'VV').replace('cc', 'CC')
    
    # 2. 자음 / 모음 / 두글자 자음 에서 검색
    i = 0
    len_text = len(text)
    last_t = text[len_text - 1]
    before_last_t = text[len_text - 2]
    while i < len_text:
        v = vc[i]
        t = text[i]
        # 한글일 경우
        try:
            if v == 'f' or v == 'c':   # 자음
                result += cons[t]
                i += 1

            elif v == 'V':   # 더블 모음
                result += vowels[text[i:i+2]]
                i += 2

            elif v == 'v':   # 모음
                result += vowels[t]
                i += 1

            elif v == 'C':   # 더블 자음
                result += cons_double[text[i:i+2]]
                i += 2
            else:
                result += t
                i += 1
                
        # 더블 모음(자음) 검색 오류 발생 시
        except KeyError:
            if t in cons:
                result += cons[t]
            elif t in vowels:
                result += vowels[t]
            i += 1

    result_1 = ''
    result_2 = join_jamos(result)
    split_index = 0
    if collapse: return result_2
    elif len(result_2) == 2:
        result_1 = result_2[0]
        result_2 = result_2[1]
        split_index = len_text - 1
        if last_t in vowels and before_last_t in cons:
            split_index -= 1

    # print(f"{result_1}, {result_2}, {split_index}")
    return result_1, result_2, split_index
