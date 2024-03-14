---
layout: post
title: Páros vagy páratlan
date: 2024-03-14 20:19
category: [feladat]
author: Veres Benedek
tags: [3, if]
summary: 
---

írj programot ami bekér egy számot a felhasználótól
és megmondja hogy az a szám páros vagy páratlan-e
megj.: az inputot áttudod alakítani integerré az int()
 x = int(input()) 


<details>
<summary>
Megoldás
</summary>

{% highlight ruby %}
```python
x = int(input())

if x % 2 == 0:
    print("Páros")
else:
    print("Páratlan")
```
{% endhighlight %}

</details>