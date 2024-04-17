---
title: Gauss-módszer
description: ""
date: 2024-04-17T06:33:50.504Z
preview: ""
tags: []
categories: [Tananyag]
type: default
---

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

# Gauss – módszer



A Gauss – módszer az egyenletrendszer mátrixát ekvivalens átalakítások segítségével úgy
rendezi át, hogy a mátrix főátlójában egyesek, a diagonális alatt pedig nullákat kapjunk. A diagonális
felett bármilyen szám valós lehet. \

<center>
$$\begin{pmatrix}
    1 & . & . &\bigm \vert   & x_{1} \\
    0 & 1 & . &\bigm \vert & x_{2} \\
    0 & 0 & 1 &\bigm \vert & x_{3} \\
\end{pmatrix}
 $$
</center>
Az ekvivalens átalakítások alkalmazása jól látható egy példán. Az egyenletrendszerünk:
<center>
$$
2𝑥_{1} + 4𝑥_{2} = 7 \\
3𝑥_{1} + 6𝑥_{2} − 𝑥_{3} = 8 \\
𝑥_{1} + 5𝑥_{2} + 𝑥_{3} = 1 \\
$$
</center>

   Az egyenletrendszer mátrixa a következő:

<center>
$$\begin{pmatrix}
    2 & 4 & 0 &\bigm \vert   & 7 \\
    3 & 6 & -1 &\bigm \vert & 8 \\
    1 & 5 & 1 &\bigm \vert & 1 \\
\end{pmatrix}
 $$
</center>

A mátrix rendezését oszloponként végzem. Elöször az első oszlopot hozom a kívánt alakra,
majd a másodikat,…
Elöször a főátlón lévő elem helyére kell egyest tennem. Ezt úgy érhetem el, hogy az első sort
elosztom azzal a számmal, amely a főátlóban van. Előfordulhat, hogy a főátlóban lévő elem nulla.
Ebben az esetben kicserélem a sort egy olyan alatta lévő sorral, ahol a megfelelő oszlopban található
szám nem nulla. (Ha nem találok ilyet, akkor az egyenletrendszernek nincs megoldása) Ezután elérem
a már említett módon, hogy a főátlón egyeseket kapjak

<center>
$$
\begin{pmatrix}
    2 & 4 & 0 &\bigm \vert   & 7 \\
    3 & 6 & -1 &\bigm \vert & 8 \\
    1 & 5 & 1 &\bigm \vert & 1 \\
\end{pmatrix}
 

\sim

\begin{pmatrix}
    1 & 2 & 0 &\bigm \vert   & \frac{7}{2} \\
    3 & 6 & -1 &\bigm \vert & 8 \\
    1 & 5 & 1 &\bigm \vert & 1 \\
\end{pmatrix}
$$
</center>

Ezután az oszlop főátló alatii elemeit nullázom a következőképpen: minden sorból kivonom a
diagonálison lelő elemet tartalmazó sor annyiszorosát, amilyen szám van azon a helyen, ahol nullát
akarok kapni.

<center>
$$
\begin{pmatrix}
    1 & 2 & 0 &\bigm \vert   & \frac{7}{2} \\
    3 & 6 & -1 &\bigm \vert & 8 \\
    1 & 5 & 1 &\bigm \vert & 1 \\
\end{pmatrix}
 

\sim

\begin{pmatrix}
    1 & 2 & 0 &\bigm \vert  & \frac{7}{2} \\
    0 & 0 & -1 &\bigm \vert & -\frac{5}{2} \\
    0 & 3 & 1 &\bigm \vert & -\frac{5}{2} \\
\end{pmatrix}
$$
</center>

Így a mátrix első oszlopának alakja már megfelelő. A második oszlopban ugyanígy járok el.
Kezdem a főátlón levő elemmel. A mi mátrixunkban ez nulla, tehát kicserélem a második sort a
harmadikkal.

<center>
$$
\begin{pmatrix}
    1 & 2 & 0 &\bigm \vert   & \frac{7}{2} \\
    0 & 0 & -1 &\bigm \vert & -\frac{5}{2} \\
    0 & 3 & 1 &\bigm \vert & -\frac{5}{2} \\
\end{pmatrix}
 

\sim

\begin{pmatrix}
    1 & 2 & 0 &\bigm \vert  & \frac{7}{2} \\
    0 & 3 & 1 &\bigm \vert & -\frac{5}{2} \\
    0 & 0 & -1 &\bigm \vert & -\frac{5}{2} \\
\end{pmatrix}
$$
</center>


Végig osztom a sort mátrix[1,1]-vel (második sor második oszlop csak 0-tól indexelve), így a
diagonálison egyeseket kapok.

<center>
$$
\begin{pmatrix}
    1 & 2 & 0 &\bigm \vert   & \frac{7}{2} \\
    0 & 3 & 1 &\bigm \vert & -\frac{5}{2} \\
    0 & 0 &-1 &\bigm \vert & -\frac{5}{2} \\
\end{pmatrix}
 

\sim

\begin{pmatrix}
    1 & 2 & 0 &\bigm \vert  & \frac{7}{2} \\
    0 & 1 & \frac{1}{3} &\bigm \vert & -\frac{5}{6} \\
    0 & 0 & -1 &\bigm \vert & -\frac{5}{2} \\
\end{pmatrix}
$$
</center>

Így folytatom a mátrix rendezését oszloponként, amíg a mátrix kívánt alakú nem lesz:

<center>
$$
\begin{pmatrix}
    1 & 2 & 0 &\bigm \vert  & \frac{7}{2} \\
    0 & 1 & \frac{1}{3} &\bigm \vert & -\frac{5}{6} \\
    0 & 0 & -1 &\bigm \vert & -\frac{5}{2} \\
\end{pmatrix}
 

\sim

\begin{pmatrix}
    1 & 2 & 0 &\bigm \vert  & \frac{7}{2} \\
    0 & 1 & \frac{1}{3} &\bigm \vert & -\frac{5}{6} \\
    0 & 0 & 1 &\bigm \vert & \frac{5}{2} \\
\end{pmatrix}
$$
</center>

A főátlóban egyeseket kaptam, a főátló alatt pedig nullákat. A mátrixhoz tartozó egyenletrenszer a
következő:

$$
𝑥_{1} + 2𝑥_{2} = \frac{7}{2} \\
𝑥_{2} − \frac{1}{3𝑥_{3}} = −\frac{5}{6} \\
𝑥_{3} = \frac{5}{2} \\ 
$$

A mátrix utolsó sorában mindenhol nulla van, cska a főátlóban van egyes. Így az utolsó ismeretlen már
ki van fejezve. A többi ismeretlen alulról felfelé haladva fokozatos visszahelyettesítéssel tudom
kiszámolni. Az egyenletrenszer gyökei a mátrix n-ik oszlopában lesznek.

$$
𝑥_{3} = \frac{5}{2} \\
𝑥_{2} + \frac{1}{3} \times \frac{5}{2} = -\frac{5}{6} \\
𝑥_{2} = -\frac{10}{6} \\
𝑥_{1} = 2 \times (−\frac{10}{6}) + 0 \times \frac{5}{2} = \frac{7}{2} \\
𝑥_{1} = \frac{41}{6} \\
$$

> *forrás: Hevesi Anikó tanárnő jegyzetei*