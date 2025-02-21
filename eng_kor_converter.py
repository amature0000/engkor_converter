from hangul_utils import join_jamos
from key_map import cons, vowels, cons_double

def engkor(text):
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
    
    # cvv → fVV / cv → fv / cc → dd 
    vc = vc.replace('cv', 'fv').replace('cvv', 'fVv').replace('ccc', 'ddd').replace('cc', 'dc')
    
    # 2. 자음 / 모음 / 두글자 자음 에서 검색
    i = 0
    while i < len(text):
        v = vc[i]
        t = text[i]

        j = 1
        # 한글일 경우
        try:
            if v == 'f' or v == 'c':   # 초성(f) & 자음(c) = 자음
                result += cons[t]

            elif v == 'V':   # 더블 모음
                result += vowels[text[i:i+2]]
                j += 1

            elif v == 'v':   # 모음
                result += vowels[t]

            elif v == 'd':   # 더블 자음
                result += cons_double[text[i:i+2]]
                j += 1
            else:
                result += t
                
        # 한글이 아닐 경우
        except KeyError:
            if t in cons:
                result += cons[t]
            elif t in vowels:
                result += vowels[t]
            elif t == ' ':
                result += ' '
            else:
                result += t
        
        i += j

    return join_jamos(result)
