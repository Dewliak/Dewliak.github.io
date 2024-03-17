---
title: A számítógép felépítése
description: ""
date: 2024-03-17T14:12:09.822Z
preview: ""
tags: []
categories: [Tananyag]
type: default
---

![comic](/assets/computer_structure_comic.jpg)

#  **A számítógép felépítése**

## **Hardware** - *a megfogható részek*

### Nuemann-elv
Neumann János fektette le a mai modern számítógép alapelveit:
1. Teljesen elektromos működés
2. Kettes számrendszer használata
3. Belső memória használata
4. Univerzális felhasználhatóság, Turing-gép (programozhatóság; a különböző feladatok programokkal legyenek megoldva, nem pedig erre a célra épített hardverrel)
5. Szerkezet: öt funkcionális egység (aritmetikai egység, központi vezérlőegység, memóriák(operatív tár), bemeneti és kimeneti egységek)
 
![Neumann-architektúra](/assets/neumann-elv.jpg)

### Perifériák:
1. **Alaplap**
    Az alaplapon találhatóak a számítógép legfontosabb részei: processzor, memória(RAM), ROM, BIOS chip, órajel generátor, csatlakozók; ezeket ősszekötő áramkör, a busz.

2. **Mikroprocesszor**/**Processzor** - *CPU*
    A számítógép legfontosabb része(*agya). Ez végzi valamennyi műveletet, irányítja a memória használatát, gondskodik a perifériák kezeléséről.

    > Első személyi számítógépet 1981-ben az IBM cég bocsátotta ki Intel 8086-os processzorral

    Jellemzők:
        - órajel sebesség - Az **órajel frekvenciáját** adja meg (GHz). Például 3 GHz azt jelenti, hogy a processzor 3 milliárd műveleti ciklust hajt végre másodpercenként. A mai gépekben általában 2-3 GHz-es processzorok vannak. 
        - adathossz = adatbusz hossza (32 bit, 64 bit) - Azt adja meg, hogy a processzor hány bites adatokat tud feldolgozni egyszerre. Minél nagyobb az érték annál kevesebb lépésben tud egy-egy elemi feladatot végrehajtani.
    - (plusz anyag) - utasítás készlet:
    >  - **RISC** - *Reduced Instruction Set Computer* - pl. ARM processzorok (Mac, telefonok)
    >  - **CISC** - *Complex Instruction Set Computer* - pl. x86 processzorok (Intel-es, AMD-s)

    1. vezérlő egység (*CU*)
        - a memóriában tárolt program dekódolásátés és  végrehajtását végzi.
        - Fontos feladata a processzor-részegységek működésének összehangolása.
    2. aritmetika és logikai egység (*ALU*)
        - a logikai és számítási műveletek látja el

        A mai processzorok ún. **regisztereket** használnak, amelyek indeiglenes adatok gyors elérését teszi lehetőve(gyorsabb mint a memória, mert ez egyenes benne van a processzorban)
    3. processzor hűtése:
       - léghűtéses - hűtőborda, hűtőpaszta
       - vízhűtéses - víz, folyékony nitrogén (szuperszámítógépeknél)
3. **Társprocesszor**
    A processzor munkáját segíti. Főleg régebben voltak elterjedtek, manapság ezek mint benne vannak a processzorokban. Ilyenek például: matematikai operációkra, floating point arithmetics (nem egészámokkal való műveletek),...  
4. **Memória** - *RAM*
    Itt tárolja a számítógép az éppen futó programokat és adatokat. A dolgok végrehajtása is innen történik. A számítógép kikapcsolásakor eltűnnek az adatok. 
    RAM-ok típusai:
    1. DRAM (Dynamic RAM) - frissítést igényel, elavult
    2. SRAM (Static RAM) - frissítést nem igénylő, ez váltota fel régebben a DRAM-ot, drága
    3. DDR-RAM (Double Data Rate - RAM) - Manapság legelterjedtebb RAM, alacsony energia igény, nagyobb adatátviteli képesség
    4. CMOS RAM - tartalmát kikapcsolás után is megtartja, a számítógép belső óráját működteti
5. **Órajel-generátor**
   Adott periódusú impulzusokkal összehangolja a számítógép működését. Minden impulzusra a gép egy alapműveletet végez el.
6. **Buszok**
    A processzort, memóriát és a bővítókártyákat ún. **buszok** kötik össze
    Fajtái:
    - **címbusz** - memória hozzáférés (memóriában adott cím hex kódok formájában van általában pl.: 0x1A)
    - **adatbusz** - itt folyik a tényleges adatforgalom.
7. **Tápegység**
    220 V-os váltakozó áramot alakít át 12 V-os egyenárammá, amely táplalja stabilan az egész gépet.
8. **Bővítő kártyák**
    Az alaplapot egészíti ki: monitorhoz, videókártya, hálózati kártya, hangkártya, I/O- és bemeneti kártyák

## Software - *nem megfogható részek*
