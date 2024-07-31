import sys
sys.stdin = open('input.txt', 'r')

test_case = int(input())

for i in range(1, test_case + 1):
    people_throw = int(input())
    rock_list = list(map(int, input(). split()))

    # 제약사항 설정
    if not 1 <= people_throw <= 1000 :
        raise ValueError
    for position in rock_list :
        if (position < -100000) or (position > 100000): # 돌 위치
            raise ValueError
    # ---------------------

    main_list = list()
    main_dict = dict()
    for rock in rock_list :
        distance = abs(rock)
        frequen = rock_list.count(distance)
        main_list.append(frequen)
        main_dict[frequen] = distance    
   
    print(f'#{i} {max(main_dict.keys())} {main_dict[frequen]}')


    
        
  