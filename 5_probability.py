import numpy as np
import random

def Q5_4():
    # P(max = 4) = P([4]) + P([<4, 4]) + P([<4, <4, 4]) + ...
    # = (1/6) + (1/2)(1/6) + (1/2)(1/2)(1/6) + ...
    # = infinite sum of (1/2)^i * (1/6)

    P_4 = 0
    for i in range(0,20000):
        P_4 += ((1/2)**i)*(1/6)
    print('P(Max = 4) = ',P_4) # 1/3

    P_5 = 0
    for i in range(0,20000):
        P_5 += (i+1)*((1/6)**2)*((4/6)**i)
    print('P(Max = 5) = ', P_5) # 1/4

    P_6 = 1-P_4-P_5
    print('P(Max = 6) = ', P_6) # 5/12

    E = 4 * P_4 + 5 * P_5 + 6 * P_6
    print(E)


def Q5_5():
    for p in range(1,10000):
        for q in range(1,10000):
            if 4 < p/q < 6 and abs(p-q) == 25:
                print(f'{p}/{q} = {p/q}')
