square = [[5,2,3],
          [4,1,6],
          [7,8,9]]

def calc_fitness(square):
    rowsum = abs(sum(square[0])-15) + abs(sum(square[1])-15) + abs(sum(square[2])-15)
    colsum = abs(square[0][0] + square[1][0] + square[2][0] - 15) + abs(square[0][1] + square[1][1] + square[2][1] - 15) + abs(square[0][2] + square[1][2] + square[2][2] - 15)
    diagsum1 = abs(square[0][0] + square[1][1] + square[2][2] - 15)
    diagsum2 = abs(square[2][0] + square[1][1] + square[0][2] - 15)
    return rowsum+colsum+diagsum1 + diagsum2

print(calc_fitness(square))

fit_dict = {}

for a_0 in range(3):
    for a_1 in range(3):
        for b_0 in range(3):
            for b_1 in range(3):
                new_square = [[1,2,3],[4,5,6],[7,8,9]]
                temp = new_square[a_0][a_1]
                new_square[a_0][a_1] = new_square[b_0][b_1]
                new_square[b_0][b_1] = temp
                if a_0 == 2 and a_1 == 1 and b_0 == 0 and b_1 == 1:
                    print('###########')
                    print(new_square)
                fit_dict[((a_0,a_1),(b_0,b_1))] = calc_fitness(new_square)

print(fit_dict)

min_key = min(fit_dict, key=fit_dict.get)
min_value = fit_dict[min_key]

print(f"Minimum key: {min_key}")
print(f"Minimum value: {min_value}")