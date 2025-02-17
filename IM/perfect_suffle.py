T = int(input())

for tc in range(1, T+1):
    N = int(input())
    card = list(input().split())
    center = N//2
    if N % 2 == 0:
        left = card[:center]
        right = card[center:]
    else:
        left = card[:center+1]
        right = card[center+1:]
        right.append('')

    perfect_card = []
    for i in range(len(right)):
        perfect_card.append(left[i])
        perfect_card.append(right[i])

    if perfect_card[-1] == '':
        perfect_card.pop()

    print(f"#{tc} {' '.join(perfect_card)}")