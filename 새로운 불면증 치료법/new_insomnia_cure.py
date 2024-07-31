import sys
sys.stdin = open("sample_input.txt", "r")

test_case = int(input())

for i in range(1, test_case + 1):
    first_num = int(input()) #1295
    second_num = first_num.copy()
    count_num = 0
    count_set = set()
    while len(count_set) < 10 :
        count_num += 1
        
        count_set.update(num for num in str(first_num))
        
        second_num * 2     
        
    print(f"#{i} {count_num}")