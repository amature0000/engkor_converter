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
    vc = vc.replace('vv', 'Vv').replace('ccc', 'CCC').replace('cc', 'Cc')
    
    # 2. 자음 / 모음 / 두글자 자음 에서 검색
    i = 0
    t = ''
    past_t = ''
    len_text = len(text)
    while i < len_text:
        past_t = t
        v = vc[i]
        t = text[i]

        j = 1
        # 한글일 경우
        try:
            if v == 'c':   # 자음
                result += cons[t]

            elif v == 'V':   # 더블 모음
                result += vowels[text[i:i+2]]
                j += 1

            elif v == 'v':   # 모음
                result += vowels[t]

            elif v == 'C':   # 더블 자음
                result += cons_double[text[i:i+2]]
                j += 1
            else:
                result += t
                
        # 더블 모음(자음) 검색 오류 발생 시
        except KeyError:
            if t in cons:
                result += cons[t]
            elif t in vowels:
                result += vowels[t]
        
        i += j
    result_1 = ''
    result_2 = join_jamos(result)
    split_index = 0
    if len(result_2) == 2:
        result_1 = result_2[:1]
        result_2 = result_2[1:]
        if t in vowels and past_t in cons:
            split_index = len_text - 2
        else:
            split_index = len_text - 1

    # print(f"{result_1}, {result_2}, {split_index}")
    return result_1, result_2, split_index
