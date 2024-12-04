import numpy as np

def Q11_1():
    params_layer1 = 425*(64*64 + 1)
    params_layer2 = 225*(425 + 1)
    params_layer3 = 80*(225 + 1)
    params_output = 6*(80+1)

    num_params = params_layer1+params_layer2+params_layer3+params_output
    print(num_params)

def Q11_3():
    params_conv1 = (5*5*3 + 1)*32     # (k_w \times k_h \times C_{in} +1)\times C_{out}
    params_pool1 = 0
    params_conv2 = (3*3*3 + 1)*16
    params_pool2 = 0
    params_linear1 =

Q11_1()