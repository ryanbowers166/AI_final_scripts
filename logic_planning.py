import numpy as np

def Q9_1():
    cases = {'A':(0,0,0,1),
             'B':(0,1,0,0),
             'C':(0,1,0,1),
             'D':(0,1,1,1),
             'E':(1,0,0,0),
             'F':(1,0,1,0),
             'G':(1,1,1,0),
             'H':(1,1,1,1),
             'Celestial':(1,1,0,1),
             'Voyager':(0,0,1,1)
             }


    for case in cases:
        CS,AW,LQ,HM=cases[case]
        l1 = CS or AW # Good
        l2 = not (AW and not LQ) # Good
        l3 = CS and not (HM == True and LQ == False) # Good
        l4 = AW and ((not LQ == CS)) # Good
        l5 = not (l1 == True and l2 == False)
        x = not (l4 == True and l3 == False)
        l6 = not ((l2 or l3) and (x == False))

        desirable = not (l5 == True and l6 == True)    # l5 implies not l6
        print(case,': ',desirable)

Q9_1()