N=int(input("tesztek szama:"))
if N < 1 or N > 1000:
    print("Hibas szam")
i=1
while i<=N:
    if N<1 or N>1000:
        break
    V=int(input("Osszeg:"))
    if V<1 or V>100000:
        print("Hibas szam, adjon meg egy szamot 1 es 100000 kozott")
    else:
        szazas=0
        otvenes=0
        tizes=0
        otos=0
        kettes=0
        egyes=0
        if V%100==0:
            szazas=V/100
        else:
            szazas = V/100
        V=V%100
        if V%50==0:
            otvenes=V/50
        else:
            otvenes = V / 50
        V=V%50

        if V%10==0:
            tizes=V/10
        else:
            tizes = V / 10
        V=V%10

        if V%5==0:
            otos=V/5
        else:
            otos = V / 5
        V=V%5

        if V%2==0:
            kettes=V/2
        else:
            kettes = V / 2
        V=V%2

        if V%2==0:
            egyes=0
        else:
            egyes=1
        if int(szazas)!=0:
            print(int(szazas), 'db', '100Ft',end="; ")
        if int(otvenes)!=0:
            print(int(otvenes),'db','50Ft',end="; ")
        if int(tizes)!=0:
            print(int(tizes),"db","10Ft",end="; ")
        if int(otos)!=0:
            print(int(otos),"db","5Ft",end="; ")
        if int(kettes)!=0:
            print(int(kettes),"db","2Ft",end="; ")
        if int(egyes)!=0:
            print(int(egyes),"db","1Ft",end="; ")
        if int(N)!=i:
            print("")
        i=i+1