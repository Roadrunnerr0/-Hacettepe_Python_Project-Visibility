# Bu program, bir çalışanın 30 günlük çalışma saatleri ve satışları üzerinden maaşını hesaplar.
# Maaş = (Toplam çalışma saati * saatlik ücret 150 TL + toplam satışın %10'u komisyon) * (1 + çalıştığı yıl / 10)
# Daha sonra brüt maaşa göre vergi kesintisi uygulanır:
# - 50.000 TL altı ise %5
# - 50.000-100.000 TL arası ise %15
# - 100.000 TL üzeri ise %35
# Net maaş = brüt maaş - vergi

kisi = "Erva"

calistigi_yıl = int(input("Erva kaç yıldır çalışıyor:"))#ervanın çalışma günü alınır

calisma_saatleri = []  # çalışılan saatleri saklayacak liste
satislar = []          # yapılan satışları saklayacak liste

# 30 gün için çalışılan saat ve satış bilgisi
for i in range(1, 31):
    calisma_saatleri.append(int(input(f"Erva {i}. gün de kaç saat çalışmıtır:")))
    satislar.append(int(input(f"Erva {i}. gün de kaç TL satış yapmıştır:")))

kazanc = 0  #kazancı sıfırdan ilk değeri veriyoruz 

# Her gün için saat başına 150tl çarpılır 
for i in calisma_saatleri:
    kazanc += i * 150

komisyon = sum(satislar) * 0.1  # satış toplamının %10'u komisyon olarak hesaplanır

# Çalışma yılı arttıkça maaş artar (örneğin 5 yıl çalışmışsa %50 artış alır)
burut_maas = (kazanc + komisyon) * (1 + (calistigi_yıl) / 10)#bürüt maaş hesaplanır 

# Vergi ve net maaş hesaplanır (maaşa göre vergi oranı artar)
if burut_maas < 50000:
    vergi = burut_maas * 0.05  # %5 vergi
    net_maas = burut_maas - vergi
elif burut_maas < 100000:
    vergi = burut_maas * 0.15  # %15 vergi
    net_maas = burut_maas - vergi
else:
    vergi = burut_maas * 0.35  # %35 vergi
    net_maas = burut_maas - vergi  

