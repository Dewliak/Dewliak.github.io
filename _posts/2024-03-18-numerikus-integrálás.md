---
title: Numerikus integrálás
description: ""
date: 2024-03-18T12:50:15.620Z
preview: ""
tags: []
categories: []
type: default
---

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

![comic](/assets/comics/calculus_comic.jpg)

A függvény határozott integráljának értéke megegyezzik az $$ <a,b> $$ intervallumon a függvény görbéje alatti terület nagyságával.

$$ T = \, \int_{a}^{b} f(x) \, dx $$

> A numerikus integrálás célja a terület meghatározása egy adott ($$ \varepsilon $$) pontossággal


## Téglalap - módszer

Az $$ <a,b> $$ intervallumot **n** darab téglalapra osztjuk. Egy része hossza így:
$$ h = \frac{b-a}{n} $$

<ins>
A téglalapok egyik hossza a h, a másik pedig a függvényérték a h hosszúságú intervallum elején.
</ins> \
Innen tehát általánosan:

$$ T = \int_{a}^{b} f(x) \, dx = h*\sum_{i=0}^{n-1}{f(a+i*h)}$$

Belátható, hogy az eredmény annál pontosabb, minnél nagyobb az **n**. Ha **n** nagyon nagy, akkor **h** értéke szinte pontszerű.  Addig növeljünk n-t, amíg a felosztáshoz tartozó <ins> területek közötti eltérés nem lesz a kívánt $$ \varepsilon $$ - nál kisebb </ins>

Program:

{% highlight python %}
def f(x):
    return x**2

def numerikus_integralas_teglalap(a,b):
    n=10
    eps = 0.001
    t = 0
    toreg = 100
    while not (abs(toreg - t) <= eps):
        toreg = t
        t = 0
        h = (b-a)/n
        for i in range(n):
            t = t + f(a+i*h)

        t = t*h
        n *= 2

    return t
{% endhighlight %}

## Trapéz - módszer
A trapéz - módszer nagyon hasonlít a téglalap - módszerrel, csak téglalapok helyett trapézokat használunk. Gyorsabban jutunk el pontos eredményekhez. 

A trapéz magassága **h**, ugyanaz mint előző esetben $$ h = \frac{b-a}{n} $$. A trapéz egyik oldala $$ f(a+i*h) $$ a h hosszúságú intervallum alsó határa, a másik $$ f(a+ (i+1)*h) $$ a h hosszúságú intervallum felső határa. 
$$ T = \frac{h}{2} \sum_{i=0}{n-1} (f(a + i*h) + f(a + (i+1)*h))  $$

A program:
{% highlight python %}
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

{% endhighlight %}

## Monte Carlo módszer

Elöször kicsit viccesen hangozhat, de egyik módja a terület meghatározásnak az, hogy egy adott téglalapba véletlenszerűen lövöldözünk pontokat. Az $$ f(x) <= y $$ feltétel segítségével megvizsgáljuk, hogy a pont a görbe felett vagy alatt van-e. Összeszámoljuk, hogy hány pont van a görbe alatt és ennek segítségével ki tudjuk fejezni a görbe alatti területet ezzel a képlettel:
$$ \frac{görbe \,alatti \, pontok \,száma}{összes \,pontok \, száma} = \frac{görbe \,alatti \, terület}{téglalap \, alatti \, terület} $$

A program:
{% highlight python %}
import random

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
{% endhighlight %}