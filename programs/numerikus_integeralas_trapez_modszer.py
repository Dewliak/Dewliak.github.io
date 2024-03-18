
def f(x):
    return x**2

def numerikus_integralas_trapez(a,b):
    n=10
    eps = 0.001
    t = 0
    toreg = 100 # ez csak, hogy eloszor elinduljon

    while not (abs(toreg - t) <= eps):
        toreg = t
        t = 0
        h = (b-a)/n
        for i in range(n):
            t = t + (f(a+i*h) + f(a+(i+1)*h))*h/2
        n *= 2

    return t


print(numerikus_integralas_trapez(3,6))
    
