ham_yorum_1 = "BUGÜN ÇOK SU İÇTİM!💧"
ham_yorum_2 = "Su İçmeyi Unuttum!🥵"

temiz_yorum_1 = ham_yorum_1.strip()
temiz_yorum_2 = ham_yorum_2.strip()

standart_yorum_1 = temiz_yorum_1.lower()
standart_yorum_2 = temiz_yorum_2.lower()

print("Ham Yorum:", ham_yorum_1)
print("Temizlenmiş Yorum:", standart_yorum_1)
print("-------")
print("Ham Yorum:", ham_yorum_2)
print("Temizlenmiş Yorum:", standart_yorum_2)
