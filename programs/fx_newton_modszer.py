
def f(x):
    # Függvényünk   
    return x*x - 4

def fd(x):
    # A függvényünk deriváltja
    return 2*x
    

def newton_modszer(xn = 10):

    eps = 0.0001


    x = 0
    while not (abs(x-xn) < eps and abs(f(xn)) < eps):
        x = xn

        xn = x - f(x)/fd(x)

    return xn

print(newton_modszer())
