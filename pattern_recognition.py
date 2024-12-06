import numpy as np


def Q8():
    min_prev = 13
    A_i = 25
    B_j = 16

    D_i_j = abs(A_i - B_j) + min_prev
    print(D_i_j)

def Q8_17():
    A = 0.5*0.15
    print('A = ',A)
    test1 = 0.019125 == max(.5*.85*.3*.15, 0.5*0.15*0.6*0.15) # Day 2, Lion

    B_path1 = 0.5*0.85*0.7*0.85 # Starting from NL on Day 1
    B_path2 = 0.5*0.15*0.4*0.85 # starting from L on day 1
    #print(B_path1, B_path2)
    B = max(B_path1, B_path2)
    print('B = ', B)

    C_path1 = 0.5*0.15*.6*.15*.6*.85
    C_path2 = .5*.85*.7*.85*.3*.85
    C_path3 = .5*.15*.4*.85*.3*.85
    C_path4 = .5*.85*.3*.15*.6*.85
    C = max(C_path1, C_path2, C_path3, C_path4)  # Max is path 2, NL-NL-L
    print('C = ', C)

    D_path1 = .5*.85*.7*.85*.3*.85*.6*.85 # NL-NL-L-L   #TODO I think this is the most likely path but try others just in case
    D_path2 = .5*.85*.7*.85*.7*.15*.3*.85
    D = max(D_path1, D_path2)
    print('D = ', D)

    #test2 = .5*.85*.7*.85*.7*.15
    #print('test2 = ', test2)

#Q8()
Q8_17()
# print(0.5*.15*.6*.15)
# print(.5*.85*.3*.15)