from random import *
f = open("tarix_s.txt", encoding="utf-8")


def random_list(listin_adi, bash, son):
    for i in range(son-bash+1):
        while True:
            x = randint(bash, son)
            if not x in listin_adi:
                listin_adi.append(x)
                break


print("Tarix oyununa xos gelmissiniz")
print("Oyunun qaydalari cox sadedir")
print("Oyuncuya suallar verilir ve oyuncu bu suallari cavablandirir.")
print("Her dogru cavaba gore 1 xal qazanirsiniz")
print("Oyun 2021-2022-ci il tarix suallarinin ilk 348-ni ehate edir")
print("Lakin oyuncu nece sual uzre oynamaq istediyini ozu sece biler")
n = int(input("Ilk sualin nomresini qeyd edin: "))
m = int(input("Son sualin nomresini qeyd edin: "))

a = []
xal = 0
random_list(a, n, m)
# print(a)
lines = f.readlines()
suals = 1
for i in a:
    sual = lines[(i-1)*6]
    for x in sual:
        if x == '.':
            baslangic = sual.index(x)
            break
    sual = sual[baslangic+1::]
    print(f"{suals}.{sual}")
    dogru_cavab = 0
    b = []
    random_list(b, 1, 5)
    z = 0
    for j in b:
        h = (i-1)*6+j
        cavab = lines[h]
        print(f"{z}){cavab[1::]}", end="")
        if cavab[0] == 's':
            dogru_cavab = z
        z += 1
    alfab = True
    while alfab:
        alfab = False
        try:
            ist_cavab = int(input("Cavabi daxil edin: "))
        except ValueError:
            alfab = True
    if ist_cavab == dogru_cavab:
        print("DOGRUDUR!")
        xal += 1
    else:
        print("YANLISDIR!")
        print("Dogru cavab:", lines[(i-1)*6+b[dogru_cavab]][1::])

    print("Sizin xaliniz:", xal)
    suals += 1
