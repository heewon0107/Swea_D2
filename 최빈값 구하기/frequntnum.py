import sys
sys.stdin = open("input.txt", "r")

test_case = int(input()) + 1

for i in range(1, test_case):
    case = int(input())
    numbers = list(map(int, input().split()))

    if len(numbers) > 1000 :
        raise ValueError("학생의 수는 1000명이다.")
    
    counted = {}
    for score in set(numbers) : # 중복 제거
        frequen = numbers.count(score)
        
        if frequen in counted :
            counted[frequen] = max(counted[frequen], score)
        else :
            counted[frequen] = score


    print(f"#{case} {counted[max(counted)]}")


