import numpy as np

def Q11_1():
    params_layer1 = 425*(64*64 + 1)
    params_layer2 = 225*(425 + 1)
    params_layer3 = 80*(225 + 1)
    params_output = 6*(80+1)

    num_params = params_layer1+params_layer2+params_layer3+params_output
    print(num_params)

Q11_1()
