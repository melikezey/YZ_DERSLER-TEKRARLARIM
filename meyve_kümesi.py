metin1 = "elma armut"
metin2 = "elma muz"

ortak_harfler = 0

for harf in metin1:
    if harf in metin2:
        ortak_harfler += 1

benzerlik = ortak_harfler / len(metin1)

print("Metin 1:", metin1)
print("Metin 2:", metin2)
print("Ortak Harf Sayısı:", ortak_harfler)
print("Benzerlik Skoru:", round(benzerlik, 2))
