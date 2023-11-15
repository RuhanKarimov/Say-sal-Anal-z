from cmath import cos

# "Xo" ı 0'a eşitledik yani Taylor serisini Maclorin serisi şeklinde yazıcaz

print("Cos(x) için hazırlanmış taylor serisine hoş geldiniz ")

n = int(input("taylor serisini kaç terimli yapmak istersiniz : "))
x = float(input("Cos(x) için radian cinsinden x değeri giriniz (pi/5 = 0.628318531): "))

ger_deg = cos(x)    # gercek deger

xler = 1            # x'ler çarpımı1
xler = float(xler)

fakt = 1            # faktoriyel
fakt = float(fakt)

tah_deg = 0         # tahmini deger
tah_deg = float(tah_deg)

for i in range(n):
    xler = 1
    fakt = 1
    for j in range(1, 2*i+1):
        xler = xler * x

    for k in range(1, 2*i+1):
        fakt = fakt * k

    if i % 2 == 0:
        tah_deg = tah_deg + xler/fakt
    else:
        tah_deg = tah_deg - xler/fakt
kesme_hatasi = ger_deg - tah_deg

print("Gercek Deger : " + str(ger_deg))
print("Tahmini Deger : " + str(tah_deg))
print("Kesme Hatasi : " + str(kesme_hatasi))
