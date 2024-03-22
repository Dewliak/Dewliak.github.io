---
title: Gyökkeresés
description: ""
date: 2024-03-18T10:21:10.385Z
preview: ""
tags: []
categories: []
type: default
---

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>


![comic](/assets/comics/function_comic.jpg)

# Függvények gyökkeresése numerikusan

Célunk, hogy egy adott függvény és a x-tengely metszéspontját megtaláljuk. Ezt többszöri helyettesítéssel érjük el. Végül egy olyan <a, b> intervallumot kapunk, melynek nagysága legfeljebb az adott **pontosság**.

Hogy a feladatot megtudjuk oldani **3** feltételnek kell teljesülnie:
1. A függvény folytonos - nincsenek benne "lyukak"
2. A függvénynek a vizsgált intervallumon 1 gyöke van
3. az intervallum egyik határán a függvényérték negatív a másikon pozitív.
   
## Fokozatos közelítő módszer

Az intervallumot felosztjuk **n** darab részre, így n darab **h** szélességű intervallumot kapunk (h = (b-a)/n). Ezután meghatározzuk a függvényértéket *a*-ban és *a+h*-ban. Ha van előjel változás, akkor a függvény, az <a, a+h> intervallumban van. Ha nincs akkor tovább csináljuk így, míg nem találunk egy olyan <a+ i*h, a + (i+1)*h>, amelyenben van előjel változás. Ekkor ez lesz az új **a,b** intervallum. Ezt addig csináljuk amíg (eps ($$ \varepsilon $$), az a pontossági tényező pl. eps = 0.001):
   1. $$ \mid b - a \mid < \varepsilon $$
   2. $$ \mid f(a) \mid < \varepsilon $$ 
      - ez azért fontos mert **nem meredek** függvénynél nem kapjuk meg a megoldást kellő pontossággal
    
Közelítő módszer program:

{% highlight python %}
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
{% endhighlight %}

Belátható, hogy feleslegesn sokszor számoljuk ki a függvényértéket, hiszen minden egyes ciklusban **2-szer** számoljuk ki, míg elég lenne **1-szer**,  ha elmentenénk.


Az optimalizált program:

{% highlight python %}
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

{% endhighlight %}

## Intervallumfelező módszer

Az egyik legegyszerűbb módszer. Lényege, hogy az $$ <a,b> $$ intervallumot felosztjuk 2 részre $$ <a, m> $$ és$$ <m, b> $$, ahol $$ m = a + \frac{b-a}{2} = \frac{a+b}{2} $$. Megvizsgáljuk, hogy melyik részen vált előjelet a **f(a)xf(m) < 0**, akkor a megoldás a $$ <a,m> $$ intervallumban van, más esetben pedig az $$ <m,b> $$. Ezután az intervallumot megint tovább osztjuk, egészen addig, amíg nem érvényes: \
<center> $$ \mid f(a) \mid < \varepsilon \  \And \mid a-b \mid < \varepsilon$$ </center>


A program:

{% highlight python %}
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
{% endhighlight %}

Hasonlóan az előző esethez ez is ugyanúgy optimalizálható:

{% highlight python %}
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
{% endhighlight %}



## Newton módszer

Ez a módszer akkor használtható nagyon effektíven, amikor ismerjük a metszéspont egy közelítő értékét.
**Lényege:** Ezen a közelítőpontnál(továbba x0) a érintőt húzunk a függvényhet. Ez az érintő az x-tengelyt metszve az **x1** pontot adja, amely jobb esetben közelebb van a gyökhöz, mint az **x0**. 

![comic](/assets/segedanyag/Newton_method.png)

Felírhatjuk az ábra alapján:

$$
    tg \alpha = \frac{f(x_{0})}{x_{0} - x_{1}}
$$

Ebből kifejezve x1-et:

$$
    x_{1} = x_{0} - \frac{f(x_{0})}{tg \alpha} =  x_{0} - \frac{f(x_{0})}{f'(x_{0})}

$$

Általános iterálós alakban:

$$
    x_{i+1} = =  x_{i} - \frac{f(x_{i})}{f'(x_{i})}

$$

Ezt addig-addig folytatjuk, amíg el nem érünk a **közelítő feltételig**: 

$$
  
  \mid x_{i+1} - x_{i} \mid < \varepsilon \  \And \mid f(x_{i}) \mid < \varepsilon

$$


A Newton módszer csak bizonyos *feltételeknél* konvergál, azaz véges számú lépés után megoldást talál:
1. $$ f(x) $$ függvénynek az $$ <a,b> $$ <ins> intervallumon csak  egyetlen gyöke van </ins>
2. Az $$ f'(x) $$ és $$ f''(x) $$ az $$ <a,b> $$ intervallumon <ins> folytonosak és nem változtatnak előjelet </ins>

A program:

{% highlight python %}
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
{% endhighlight%}

*forrás: Hevesi Anikó tanárnő jegyzetei*