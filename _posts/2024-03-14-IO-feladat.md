---
title: IO feladat
date: 2024-03-14 20:12
category: [feladat]
author: Veres Benedek
tags: [1,IO]
---

1. Készíts egy programot, amely üdvözöl
2. Megkéri a felhasználót, hogy adjon meg egy települést
3. Adja meg a felhasználó a kedvenc dolgát
4. Kombináld a kettőt és írd ki

<details>
<summary>
HINTS
</summary>

{% highlight ruby %}
1. használd a kombinációhoz +-t vagy ,-t
{% endhighlight %}
</details>

<details>
<summary>
Megoldás
</summary>

{% highlight ruby %}
```python
# 1. Készíts egy programot, amely üdvözöl
print("Hello a név generátor programban")

# 2. Megkéri a felhasználót, hogy adjon meg egy települést
telepules = input("Adj meg egy települést:")

# 3. Adja meg a felhasználó a kedvenc dolgát
kedvenc = input("Add meg a kedvenc dolgod:")

# 4. Kombináld a kettőt és írd ki
print("A banda neve: " + telepules + " " + kedvenc)
```
{% endhighlight %}

</details>