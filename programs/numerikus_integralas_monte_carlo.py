
import random

def f(x):
    return x**2

def numerikus_integralas_monte_carlo(a,b,magassag=100, n = 10000):
    
    alatt = 0

    for i in range(n):

        x = a +(b-a)*random.random()
        y = magassag*random.random()

        if y <= f(x):
            alatt += 1

    n = alatt/n

    terulet = magassag*(b-a)*n

    return terulet
    
print(numerikus_integralas_monte_carlo(2,4))
    
