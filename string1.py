# 문자열 비교

def equal_str(s1, s2):
    N = len(s1)
    M = len(s2)

    for i in range(M-N-1):
        if str2[i:i+N] == str1:
            return 1
    return 0


T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    print(f"#{tc} {equal_str(str1, str2)}")

# 글자수


def equal_char(s1, s2):

    N = len(s2)
    most_char = 0

    for char in s1:  # s1 문자열을 순회해서 1글자씩 꺼내기
        char_count = 0  # 꺼낸 char의 개수 카운트
        for i in range(N):  # s2 순회하면서 char와 비교
            if s2[i] == char:
                char_count += 1
                # s2 순회가 끝나고 최종 char_count와 most_char비교해서 최대값 구하기
            most_char = max(char_count, most_char)

    return most_char


T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    print(f"#{tc} {equal_char(str1, str2)}")


# 문자열의 거울상

def bq_mirror(s):
    N = len(s)
    new_s = ''

    # s를 뒤에서부터 순회하며 서로 대칭되는 모양의 알파벳을 new_s에 더해주는 방싟
    for i in range(N-1, -1, -1):
        if s[i] == 'b':
            new_s = new_s + 'd'
        elif s[i] == 'd':
            new_s = new_s + 'b'
        elif s[i] == 'q':
            new_s = new_s + 'p'
        elif s[i] == 'p':
            new_s = new_s + 'q'
    return new_s


T = int(input())
for tc in range(1, T+1):
    st = input()

    print(f"#{tc} {bq_mirror(st)}")

# 의석이의 세로로 말해요

def es_talk_col(wl):
    col_talk = ''  # 새로 읽기

    long = 0
    # 가장 긴 문자열 길이 찾기
    for st in wl:
        st_len = len(st)
        long = max(long, st_len)

    for i in range(long):
        for st in wl:
            try:
                col_talk = col_talk + st[i]  # 세로로 읽으면서 추가하기
            except IndexError:  # 글자가 없으면 넘어가기
                pass

    return col_talk


T = int(input())
for tc in range(1, T+1):
    N = 5  # 만들 단어의 수
    word_list = []
    for _ in range(N):
        word = input()
        word_list.append(word)

    print(f"#{tc} {es_talk_col(word_list)}")

# GNS

def str_num_sort(wl):
    word_num_dict = {
        "ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4,
        "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9,
    }
    
    word_num_lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    word_num_num = [x for x in range(10)]

    word_num_sort = []  # 단어를 int로 바꿔서 저장할 빈 리스트 생성
    
    # wl을 word_num_dict를 참고해서 (int)번호로 넣기
    for st in wl:
        word_num_sort.append(word_num_dict[st])
    
    word_num_sort.sort()  # 번호를 오름차순으로 정렬
    final = []  # int를 다시 word로 바꿔서 넣어 줄 리스트 생성

    for item in word_num_sort:
        for i in range(10):
            if item == word_num_num[i]:
                final.append(word_num_lst[i])  # 번호에 맞는 단어를 두 리스트의 인덱스로 매칭시켜 추가

    return ' '.join(final)


T = int(input())
for tc in range(1, T+1):
    tc_info = list(map(str, input().split()))
    word_list = list(map(str, input().split()))

    print(f"#{tc}")
    print(f"{str_num_sort(word_list)}")

# 초심자의 회문 검사

def palindrome(st):
    new_st = ''
    st_len = len(st)
    for i in range(st_len-1, -1, -1):
        new_st = new_st + st[i]

    if st == new_st:
        return 1
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    word = input()

    print(f"#{tc} {palindrome(word)}")