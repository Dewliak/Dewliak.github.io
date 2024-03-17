

def f(x):
    return 2*x - 4


def intervallumfelezo_modszer_sima(a = -100,b = 100):

    eps = 0.00001

    while not (abs(b-a)<eps and abs(f(a)) < eps):
        m = (a+b)/2

        if f(a)*f(m) < 0:
            b = m
        else:
            a = m

    return a

def intervallumfelezo_modszer_optimalizalt(a = -100,b = 100):

    eps = 0.00001
    fa = f(a)
    
    while not (abs(b-a)<eps and abs(f(a)) < eps):
        m = (a+b)/2
        fm = f(m)
        if fa*fm < 0:
            b = m
        else:
            a = m
            fa = fm

    return a


print(intervallumfelezo_modszer())
