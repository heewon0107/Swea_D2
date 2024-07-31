import sys
sys.stdin = open('input.txt', 'r')

# A 요금 함수
def water_fee_A(basic_fee, litter):
    return basic_fee * litter

# B 요금 함수
def water_fee_B(default, litter_min, over_fee, litter) :
    if litter <= litter_min :
        return default
    else : 
        return default + over_fee * (litter - litter_min)
    

test_case = int(input())

for i in range(1, test_case + 1):
    P, Q, R, S, W = map(int, input(). split())
    price_A = water_fee_A(P,W)
    price_B = water_fee_B(Q,R,S,W)
    if price_A < price_B :
        print(f"#{i} {price_A}")
    else :
        print(f"#{i} {price_B}")
        


    