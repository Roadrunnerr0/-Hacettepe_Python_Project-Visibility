sayılar = []
while True:
    try:
        adet = int(input("kaç adet sayı girmek istiyorsunuz: "))
        if adet <=0:
            print("Lütfen bir sayı giriniz: ")
            continue
        break
    except ValueError:
        print("lütfen geçerli bir sayı giriniz: ")

print(f"\n{adet} adet sayı girmeniz gerekiyor ")

#bitti komutu yerine daha işlevsel buldum

for i in range(adet):
    while True:  
        try:
            sayı = float(input(f"{i+1}. sayıyı giriniz. "))
            sayılar.append(sayı)
            break
        except ValueError:
            print("lütfen geçerli bir sayı giriniz ")
print("teşekkürler sayı girişiniz tamamlanmıştır. ")

#En küçük en Büyük sayıları bulma
en_kucuk = sayılar[0]
en_buyuk = sayılar[0]
toplam = 0

for sayı in sayılar:
    if sayı < en_kucuk:
        en_kucuk = sayı
    if sayı > en_buyuk:
        en_buyuk = sayı
    toplam += sayı

#aritmatik ortalam

ortalama = toplam / len(sayılar)

#mod hesaplama

sayı_frekans = {}
for sayı in sayılar:
    if sayı in sayı_frekans:
        sayı_frekans[sayı] += 1
    else:
        sayı_frekans[sayı] = 1

mod = max(sayı_frekans.items(), key = lambda x: x[1])[0]

print(f"En küçüğü: {en_kucuk}")
print(f"En büyüğü: {en_buyuk}")
print(f"Aritmetik ortalaması: {ortalama:.2f}")
print(f"Mod değeri: {mod}")