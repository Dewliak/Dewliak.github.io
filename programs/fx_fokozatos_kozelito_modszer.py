

def f(x):
    # Függvényünk, megoldása x = 2
    return 2*x -4 


def kozelito_modszer_sima(a = -100,b = 100,n=10):

    eps = 0.00001

    while not (abs(b-a) < eps and f(a) < eps):

        h = abs(b-a)/n

        # Az f(a)-t és az f(a+h)-t feleslegesen sokszor számoljuk ki
        while f(a)*f(a+h) > 0:
            a = a + h

        b = a + h
        
    return a

def kozelito_modszer_optimalizalt(a = -100,b = 100,n=10):

    eps = 0.00001
    # abs(f(a)) - ez nélkül nem kaptánk elég pontos megoldást
    while not (abs(b-a) < eps and abs(f(a)) < eps):

        h = abs(b-a)/n

        # Optimalizalt rész, csak egyszer számoljuk ki
        fa = f(a)
        ff = f(a+h)
        
        while fa*ff > 0:
            fa = ff
            a = a + h

            ff = f(a+h)

        b = a + h
        
    return a



