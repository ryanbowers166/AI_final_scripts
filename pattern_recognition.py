import numpy as np

def Q7_10():
    feeding = 3
    migrating = 3
    resting = 2
    p_feeding = 3/8
    p_migrating = 3/8
    p_resting = 2/8

    entropy = -(p_feeding*np.log2(p_feeding)) - (p_migrating*np.log2(p_migrating)) - (p_resting*np.log2(p_resting))
    print(entropy)

def Q8():
    min_prev = 13
    A_i = 25
    B_j = 16

    D_i_j = abs(A_i - B_j) + min_prev
    print(D_i_j)

Q8()