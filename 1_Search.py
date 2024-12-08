import numpy as np

def Q1_1():
     nodes = ['E1','E2','E3','E4','M1','M2',"M3","M4","M5",'J1','J2','J3','S1','S2','S3','S4']

     heuristic = {'E1':30, 'E2':30, 'E3':30, 'E4':30,
          'M1':20, 'M2': 20, 'M3': 20, 'M4': 20, 'M5': 20,
          'J1':10, 'J2': 10, 'J3': 10,
          'S1':0, 'S2':0, 'S3':0, 'S4':0}

     costs = {('E1','E2'):2,('E2','E3'):3,('E3','E4'):4,('E4','E1'):5,
              ('E3','M3'):10,('M3','M4'):2,('M4','M5'):3,('M5','M1'):4,('M1','M2'):1,('M2','M3'):2,('M3','S4'):30,
              ('M5','J2'):10,('J2','J3'):4,('J3','J1'):5,('J1','J2'):3,('J3','S4'):10,
              ('S4','S1'):3,('S1','S2'):2,('S1','E1'):9,('S2','S3'):2,('S3','S4'):3}

     def check_consistency(h,node1,node2,cost):
          h_n = h[node1]
          h_nprime = h[node2]
          if h_n <= h_nprime + cost:
              return True
          else:
              print(h_n)
              print(h_nprime)
              print(cost)
              print(f'h({node1}) <= cost({node1}->{node2}) + h({node2} ? ')
              print(f'{h_n} <= {cost}+ {h_nprime}')
              return False

     consistent = True
     for node_a in nodes:
          for node_b in nodes:
               if (node_a,node_b) in costs:
                    check = check_consistency(heuristic,node_a,node_b,costs[(node_a,node_b)])
                    if not check:
                         consistent = False
                         print(node_a, node_b, check)
                         break
     if consistent: print('Q 1.1: H is consistent for all parent-child node pairs\n')
     else: print('Q 1.1: H IS NOT CONSISTENT\n')


def Q1_3():
     nodes = ['E1', 'E2', 'E3', 'E4', 'M1', 'M2', "M3", "M4", "M5", 'J1', 'J2', 'J3', 'S1', 'S2', 'S3', 'S4']

     heuristic = {'E1': 30, 'E2': 30, 'E3': 30, 'E4': 30,
                  'M1': 20, 'M2': 20, 'M3': 20, 'M4': 20, 'M5': 20,
                  'J1': 10, 'J2': 10, 'J3': 10,
                  'S1': 0, 'S2': 0, 'S3': 0, 'S4': 0}

     true_cost = {'E2':2,'E3':5,'E4':9,
          'M3':15,'M4':17,'M5':20,'M1':24,'M2':25,
                  'J2':30,'J3':34,'J1':39,
                  'S4':44,'S1':47,'S2':49,'S3':51}

     print('#### Q 1.3 ####')
     for node in nodes:
          if node in true_cost:
               check = 30 <= true_cost[node]
               #print(node,check)
               if check:
                   print('H is admissible for',node)
               if not check: print('H IS NOT ADMISSIBLE FOR',node)
     print('#### Q 1.3 complete ####')

#Q1_1()
Q1_3()