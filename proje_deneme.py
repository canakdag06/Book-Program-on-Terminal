from kutuphane import *

print("""********************************
\t\t---KİTAPLIK---
1. Kitapları Göster
2. Kitap Sorgula
3. Kitap Ekle
4. Kitap Sil
5. Baskı Yükselt
Çıkmak için ->>> Q
********************************""")

kutuphane = Kutuphane()

while True:
    op = input("İşlemi girin: ")

    if op == "Q" or op == "q":
        print("Program sonlandırılıyor...")
        break
    elif op == "1":
        kutuphane.kitaplari_goster()
    elif op == "2":
        isim = input("Sorgulamak istediğiniz kitabı girin: ")
        print("Kitap sorgulanıyor...")
        time.sleep(3)
        kutuphane.kitap_sorgula(isim)
    elif op == "3":
        isim = input("İsim: ")
        yazar = input("Yazar: ")
        yayinevi = input("Yayınevi: ")
        tur = input("Tür: ")
        while True:
            try:
                baski = int(input("Baskı: "))
                if(type(baski) is int):
                    break
            except ValueError:
                print("Lütfen Tamsayı Girin.")
        yeni_kitap = Kitap(isim, yazar, yayinevi, tur, baski)
        print("Kitap Ekleniyor...")
        time.sleep(2)
        kutuphane.kitap_ekle(yeni_kitap)
        print("Kitap Eklendi.")
    elif op == "4":
        isim = input("Hangi kitabı silmek istiyorsunuz?: ")
        cevap = input("Emin misiniz? (E/H): ")
        if cevap == "E" or cevap == "e":
            kutuphane.kitap_sil(isim)
    elif op == "5":
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz?: ")
        print("Baskı yükseltiliyor...")
        time.sleep(2)
        print("Baskı yükseltildi.")
        kutuphane.baski_yukselt(isim)
    else:
        print("Geçersiz işlem.")
