import numpy as np


def Q7_1():
    def N(x,mu,sigma):
        # x is np.array
        a, b, c, d = sigma[0][0], sigma[0][1], sigma[1][0], sigma[1][1]

        det_sigma = sigma[0][0] * sigma[1][1]
        inverse_sigma = np.array([[d, -b],[-c,a]]) / det_sigma
        coeff = 1/(2*np.pi*np.sqrt(det_sigma))

        x_min_mu = (x[0]-mu[0],x[1]-mu[1])
        exponent = -0.5*np.dot(np.dot(x_min_mu, inverse_sigma), x_min_mu)
        out = coeff*np.exp(exponent)

        return out

    mu_1 = np.array([10,30])
    sigma_1 = np.array([[5, 0],[0, 5]])
    mu_2 = np.array([18,45])
    sigma_2 = np.array([[8, 0], [0, 8]])

    x_1 = np.array([15,40])
    n_1 = N(x_1,mu_1,sigma_1)
    n_2 = N(x_1, mu_2, sigma_2)

    gamma_1 = (0.5*n_1)/(0.5*n_1 + 0.5*n_2)
    gamma_2 = (0.5*n_2)/(0.5*n_1 + 0.5*n_2)
    print(gamma_1,gamma_2)
    print(gamma_1+gamma_2)


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


def Q7_10():
    feeding = 3
    migrating = 3
    resting = 2
    p_feeding = 3/8
    p_migrating = 3/8
    p_resting = 2/8

    entropy = -(p_feeding*np.log2(p_feeding)) - (p_migrating*np.log2(p_migrating)) - (p_resting*np.log2(p_resting))
    print(entropy)

Q7_1()
#Q7_10()