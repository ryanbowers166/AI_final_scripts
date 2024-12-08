import numpy as np

P_C = {'Normal': {}, 'Increased': {}}  # Returns [P(C=Absent), P(C=Present)]
P_C['Normal']['Not Triggered'], P_C['Normal']['Triggered'] = {},{}
P_C['Increased']['Not Triggered'], P_C['Increased']['Triggered'] = {},{}
P_C['Normal']['Not Triggered']['Effective'] = [0.8,0.2]
P_C['Normal']['Not Triggered']['Ineffective'] = [0.6,0.4]
P_C['Normal']['Triggered']['Effective'] = [0.4,0.6]
P_C['Normal']['Triggered']['Ineffective'] = [0.7,0.3]
P_C['Increased']['Not Triggered']['Effective'] = [0.6,0.4]
P_C['Increased']['Not Triggered']['Ineffective'] = [0.8,0.2]
P_C['Increased']['Triggered']['Effective'] = [.3,.7]
P_C['Increased']['Triggered']['Ineffective'] = [.5,.5]

P_D = {'Low': 0.6, 'High': 0.4}

P_S = {'Absent': .7, 'Present': .3}

P_M = {'Low': {'Absent':{},'Present':{}}, 'High': {'Absent':{},'Present':{}}}  # Absent, Present
P_M['Low']['Absent']['Absent'] = 0.7
P_M['Low']['Absent']['Present'] = 0.3
P_M['Low']['Present']['Absent'] = .4
P_M['Low']['Present']['Present'] = .6
P_M['High']['Absent']['Absent'] = .5
P_M['High']['Absent']['Present'] = .5
P_M['High']['Present']['Absent'] = .2
P_M['High']['Present']['Present'] = .8

P_R = {'Low': {'Absent':{},'Present':{}}, 'High': {'Absent':{},'Present':{}}}  # Effective, Ineffective
P_R['Low']['Absent']['Effective'] = .7
P_R['Low']['Absent']['Ineffective'] = .3
P_R['Low']['Present']['Effective'] = .6
P_R['Low']['Present']['Ineffective'] = .4
P_R['High']['Absent']['Effective'] = .5
P_R['High']['Absent']['Ineffective'] = .5
P_R['High']['Present']['Effective'] = .4
P_R['High']['Present']['Ineffective'] = .6

#P_A = {'Absent': [.8, .2], 'Present': [.4, .6]}  # Not Triggered, Triggered
P_A = {'Absent': {}, 'Present': {}}  # Not Triggered, Triggered
P_A['Absent']['Not Triggered'] = .8
P_A['Absent']['Triggered'] = .2
P_A['Present']['Not Triggered'] = .4
P_A['Present']['Triggered'] = .6

P_P = {'Absent':{},'Present':{}} # Normal, Increased
P_P['Absent']['Normal'] = .6
P_P['Absent']['Increased'] = .4
P_P['Present']['Normal']  = .3
P_P['Present']['Increased'] = .7


def Q6_3(P_C, P_D, P_S, P_M, P_R,P_A,P_P):
    numerator = 0
    for R in ['Effective','Ineffective']:
        for A in ['Triggered','Not Triggered']:
            for P in ['Normal','Increased']:
                for C in [0,1]:
                    numerator += P_C[P][A][R][C] * P_D['High'] * P_A['Absent'][A] * P_M['High']['Absent'][0] * P_R['High']['Absent'][R] * P_P['Absent'][P] * P_S['Absent']

    denominator = 0
    for R in ['Effective','Ineffective']:
        for A in ['Triggered','Not Triggered']:
            for P in ['Normal','Increased']:
                for C in [0,1]:
                    for D in ['Low','High']:
                        denominator += P_C[P][A][R][C] * P_D[D] * P_A['Absent'][A] * P_M[D]['Absent'][0] * P_R[D]['Absent'][R] * P_P['Absent'][P] * P_S['Absent']

    print(f'Answer = {numerator}/{denominator} = {numerator / denominator}')


def Q6_4(P_C, P_D, P_S, P_M, P_R,P_A,P_P):
    # What is P(C=Present | R=Effective, A = Not Triggered, M = Absent)?
    # Need to calculate numerator/denominator.
    # Numerator = P(+C, R=Eff, A=NT, M=Abs, D, P, S) = sum_P sum_D sum_S [(+C|P, A=Not Triggered, R=Effective)  *  P(D)  *  P(A=NotTriggered|M=Absent)  *  P(M=Absent|D,S)  *  P(R=Effective|D,M=Absent)  *  P(P|M=Abs)  *  P(S)]
    # Denominator = P(C, R=Effective, A=NT, M=Abs, D,P,S)

    # Numerator = sum_P sum_D sum_S [(+C|P, A=Not Triggered, R=Effective)  *  P(D)  *  P(A=NotTriggered|M=Absent)  *  P(M=Absent|D,S)  *  P(R=Effective|D,M=Absent)  *  P(P|M=Abs)  *  P(S)]
    numerator = 0
    for D in ['Low','High']:
        for P in ['Normal','Increased']:
            for S in ['Absent','Present']:
                numerator += P_C[P]['Not Triggered']['Effective'][1] * P_D[D] * P_A['Absent'][0] * P_M[D][S][0] * P_R[D]['Absent'][1] * P_P['Absent'][P] * P_S[S]

    # Denominator = P(C, R=Effective, A=NT, M=Abs, D,P,S)
    denominator = 0
    for C in [0,1]:
        for D in ['Low','High']:
            for P in ['Normal','Increased']:
                for S in ['Absent','Present']:
                    denominator += P_C[P]['Not Triggered']['Effective'][C] * P_D[D] * P_A['Absent'][0] * P_M[D][S][0] * P_R[D]['Absent'][1] * P_P['Absent'][P] * P_S[S]

    print(f'Answer = {numerator}/{denominator} = {numerator/denominator}')
    p = 7
    q = 25
    print(f'Answer = {p}/{q} = {p/q}')
    print(f'abs(p - q) = {abs(p-q)}')


def Q6_5(P_C, P_D, P_S, P_M, P_R,P_A,P_P):
    # What is P(P = Increased | R=Ineffective, A=Triggered)?
    # P(P=Increased, R=Ineffective, A=Triggered)  /  P(R=Ineffective, A=Triggered)
    # numerator = sum_D,S,M,C
    A = 'Triggered'
    R = 'Ineffective'

    numerator = 0
    for D in ['Low','High']:
        for M in ['Absent','Present']:
            for S in ['Absent','Present']:
                for C in [0,1]:
                    numerator += P_C['Increased'][A][R][C] * P_D[D] * P_A[M][A] * P_M[D][S][M] * P_R[D][M][R] * P_P[M]['Increased'] * P_S[S]

    # numerator = sum_D,S,M,C,P
    denominator = 0
    for D in ['Low','High']:
        for M in ['Absent','Present']:
            for S in ['Absent','Present']:
                for C in [0,1]:
                    for P in ['Normal','Increased']:
                        denominator += P_C[P][A][R][C] * P_D[D] * P_A[M][A] * P_M[D][S][M] * P_R[D][M][R] * P_P[M][P] * P_S[S]
    print(f'Answer = {numerator}/{denominator} = {numerator / denominator}')
    print(numerator/denominator - 2038/3205)
    print(2038+3205)


def Q6_6(P_C, P_D, P_S, P_M, P_R, P_A, P_P):
    # Query = P(P=Increased)
    # Evidence = R = Ineffective, A = Triggered, M = present
    R = 'Ineffective'
    A = 'Triggered'
    M = 'Present'

    # Num: Sum over D,S,C
    numerator = 0
    for D in ['Low', 'High']:
        for S in ['Absent', 'Present']:
            for C in [0, 1]:
                numerator += P_C['Increased'][A][R][C] * P_D[D] * P_A[M][A] * P_M[D][S][M] * P_R[D][M][R] * P_P[M]['Increased'] * P_S[S]
    denominator = 0
    for D in ['Low', 'High']:
        for S in ['Absent', 'Present']:
            for C in [0, 1]:
                for P in ['Normal','Increased']:
                    denominator += P_C[P][A][R][C] * P_D[D] * P_A[M][A] * P_M[D][S][M] * P_R[D][M][R] * P_P[M][P] * P_S[S]
    print(f'Answer = {numerator}/{denominator} = {numerator / denominator}')


#Q6_3(P_C, P_D, P_S, P_M, P_R,P_A,P_P)
#Q6_4(P_C, P_D, P_S, P_M, P_R,P_A,P_P)
#Q6_5(P_C, P_D, P_S, P_M, P_R, P_A, P_P)
#Q6_6(P_C, P_D, P_S, P_M, P_R, P_A, P_P)