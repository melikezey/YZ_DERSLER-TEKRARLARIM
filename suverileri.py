ham_su_verileri = [5, 6, None, 7, 4, None, 6]

temiz_su_verileri = []

for su in ham_su_verileri:
    if su is not None:
        temiz_su_verileri.append(su)

print("Ham Su Verisi:", ham_su_verileri)
print("Eksik Veriler Ayıklandıktan Sonra:", temiz_su_verileri)

ortalama_su = sum(temiz_su_verileri) / len(temiz_su_verileri)
print("Günlük Ortalama Su Tüketimi:", round(ortalama_su, 1), "bardak")
