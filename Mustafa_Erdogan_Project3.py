en_kucuk = None
en_buyuk = None #bir değişkenin henüz bir değeri olmadığında none yazilir 
toplam = 0
adet = 0
sayilar = [] #boş bir liste oluşturuyporuz burada ise biraz donra buranın içine sayilarimiz gelecek 

while True: # while döngümüzü True diyerek actik
    giris = input("Sayi: ")
    if giris.lower() == 'bitti': #burada .lower kullanıyoruz çünkü girdiğimiz strler ne olursa olsun kğçğk harfli algılanacaktır
        if adet == 0:
            print("Lütfen sayi giriniz!!")
            continue # bunları yaparken sistemimiz duraksaması için continue kullandik eğer break kullansaysik sistem burada bitecekti
        else: #şimdi ise buradaki sayimiza isteddiğimiz gibi işlemler yapabileceğiz
            print("Teşekkürler sayi girişi tamamlanmiştir.")
            ortalama = toplam / adet
            # En küçük ve en büyük değerleri for döngüsüyle buluyoruz
            for sayi in sayilar:  #program başlarken en_kucuk = None olarak tanımlandı çünkü elimizde hiç sayı yoktu
                if en_kucuk is None or sayi < en_kucuk:  #eğer direkt sayi < en_kucuk diye kontrol edersek, None ile sayı karşılaştırılamayacağı için hata alırız
                    en_kucuk = sayi  #bu yüzden önce en_kucuk is None diyerek kontrol ediyoruz
                if en_buyuk is None or sayi > en_buyuk:
                    en_buyuk = sayi

            print(f"Girilen {adet} tane sayinin, en küçüğü {en_kucuk}, en büyüğü {en_buyuk} ve aritmetik ortalamasi {ortalama} dir.")
            break
    try: # burada sistemimiz hata vermemesi için try çaliştirdik
        sayi = float(giris)
        sayilar.append(sayi) #her sayi eklediğimiz zaman listemize eklenmesi için append kullandık 
        toplam += sayi # her sayida işlem yapilacak sayi adetini arttırıyoruz
        adet += 1
    except ValueError:
        print("Lütfen geçerli bir sayi giriniz veya 'bitti' yazarak bitiriniz.")
