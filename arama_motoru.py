urunler = [
    # Üst giyim
    "Kadın Tişört",
    "Erkek Tişört",
    "Oversize Tişört",
    "Baskılı Tişört",
    "Crop Tişört",
    "Kadın Gömlek",
    "Erkek Gömlek",
    "Keten Gömlek",
    "Sweatshirt",
    "Kadın Kazak",
    "Erkek Kazak",
    "Kadın Hırka",

    # Alt giyim
    "Kadın Pantolon",
    "Erkek Pantolon",
    "Kot Pantolon",
    "Mom Jean",
    "Kargo Pantolon",
    "Eşofman Altı",
    "Kadın Etek",
    "Mini Etek",
    "Kot Etek",
    "Kadın Şort",
    "Kot Şort",

    # Elbiseler ve dış giyim
    "Kadın Elbise",
    "Abiye Elbise",
    "Çiçekli Elbise",
    "Kadın Ceket",
    "Deri Ceket",
    "Kot Ceket",
    "Kadın Mont",
    "Erkek Mont",
    "Şişme Mont",
    "Kadın Kaban",
    "Trençkot",

    # Spor giyim
    "Kadın Eşofman Takımı",
    "Erkek Eşofman Takımı",
    "Spor Tayt",
    "Spor Tişört",
    "Spor Şort",

    # Ayakkabılar
    "Spor Ayakkabı",
    "Sneaker",
    "Topuklu Ayakkabı",
    "Babet",
    "Kadın Bot",
    "Erkek Bot",
    "Kadın Sandalet",
    "Ev Terliği",

    # Çantalar ve aksesuarlar
    "Kadın Çanta",
    "Sırt Çantası",
    "Omuz Çantası",
    "Spor Çantası",
    "Şapka",
    "Bere",
    "Atkı",
    "Kemer",

    # Diğer
    "Kadın Pijama",
    "Erkek Pijama",
    "Çocuk Tişört",
    "Çocuk Mont"
]

es_anlamli = {
    "tişört": ["tshirt"],
    "tshirt": ["tişört"],
    "kot": ["jean"],
    "jean": ["kot"],
    "sweatshirt": ["hoodie"],
    "spor ayakkabı": ["sneaker"],
    "sneaker": ["spor ayakkabı"],
    "çanta": ["bag"],
    "bag": ["çanta"],
    "kadın": ["bayan"],
    "bayan": ["kadın"],
    "erkek": ["bay"],
    "bay": ["erkek"]
}

arama = input("Aramak istediğiniz ürünü girin: ").casefold()

aranacak = [arama]

for kelime, alternatifler in es_anlamli.items():
    if kelime in arama:
        aranacak.extend(alternatifler)

bulunan = []

for urun in urunler:
    for kelime in aranacak:
        if kelime in urun.casefold():
            if urun not in bulunan:
                bulunan.append(urun)

print("\nArama:", arama)

if bulunan:
    for urun in bulunan:
        print("-", urun)

    print("Toplam bulunan ürün:", len(bulunan))
else:
    print("Ürün bulunamadı.")
