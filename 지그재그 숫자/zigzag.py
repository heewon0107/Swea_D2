test_case = int(input())

for i in range(1, test_case + 1):
    num = int(input())
    
    # 제약사항 =    =   =   =
    if not 1 <= num <= 10 :
        raise ValueError
    # 제약사항 =    =   =   =
    x = 0
    sum = 0
    while x < num :
        x += 1 
        if x % 2 == 0 :
            sum -= x
        else :
            sum += x
    print(f"#{i} {sum}")

   