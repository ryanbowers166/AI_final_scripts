import numpy as np
from scipy.stats import multivariate_normal

# Create a multivariate normal distribution object
def responsibility():
    gauss_1 = multivariate_normal(mean=[10,30], cov=[[5, 0], [0, 5]])
    gauss_2 = multivariate_normal(mean=[18,45], cov=[[8, 0], [0, 8]])
    x = [15, 40]
    pdf_value = gauss_1.pdf(x)

    print("PDF at x:", pdf_value)

    responsibility_1 = (0.5*gauss_1.pdf(x))/(0.5*gauss_1.pdf(x)+0.5*gauss_2.pdf(x))
    responsibility_2 = (0.5*gauss_2.pdf(x))/(0.5*gauss_1.pdf(x)+0.5*gauss_2.pdf(x))
    print(responsibility_1)
    print(responsibility_2)

def Q7_7():
    def bic(p,n,l):  #Q7.7)
        return p*np.log(n)-2*l
    n = 10000
    bic_A = bic(3,n,-12000)
    bic_B = bic(6,n,-11500)
    bic_C = bic(12,n,-10800)
    bic_D = bic(20,n,-9500)
    bic_E = bic(35,n,-9400)

    print(bic_A,bic_B,bic_C,bic_D,bic_E)



#Q7_10()
