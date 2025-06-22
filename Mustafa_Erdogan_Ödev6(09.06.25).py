import math  # Matematiksel işlemler için math kütüphanesi kullanılıyor (√, atan2 gibi)

# KompleksSayi adında bir sınıf tanımlıyoruz
class KompleksSayi:
    def __init__(self, gercek_kisim, sanal_kisim):  # Sınıf ilk tanımlandığında çalışan yapıcı metot
        self.gercek = gercek_kisim   # Gerçek (reel) kısmı sınıf değişkenine atıyoruz
        self.sanal = sanal_kisim     # Sanal kısmı sınıf değişkenine atıyoruz

    def __str__(self):  # Nesne ekrana yazdırıldığında nasıl görünsün?
        return f"gerçek kısmı {self.gercek} sanal kısmı {self.sanal} olan {self.gercek}+{self.sanal}i kompleks sayısı"

    def __add__(self, diger):  # Toplama işlemi tanımlanıyor (self + diger)
        return KompleksSayi(self.gercek + diger.gercek, self.sanal + diger.sanal)  # Gerçek ve sanal kısımlar toplanır

    def __sub__(self, diger):  # Çıkarma işlemi (self - diger)
        return KompleksSayi(self.gercek - diger.gercek, self.sanal - diger.sanal)  # Gerçek ve sanal kısımlar çıkarılır

    def __mul__(self, diger):  # Çarpma işlemi
        yeni_gercek = self.gercek * diger.gercek - self.sanal * diger.sanal  # (a*c - b*d)
        yeni_sanal = self.gercek * diger.sanal + self.sanal * diger.gercek  # (a*d + b*c)
        return KompleksSayi(yeni_gercek, yeni_sanal)  # Yeni kompleks sayı döner

    def __truediv__(self, diger):  # Bölme işlemi (self / diger)
        payda = diger.gercek**2 + diger.sanal**2  # Payda değeri c² + d²
        yeni_gercek = (self.gercek * diger.gercek + self.sanal * diger.sanal) / payda  # Payın gerçek kısmı
        yeni_sanal = (self.sanal * diger.gercek - self.gercek * diger.sanal) / payda  # Payın sanal kısmı
        return KompleksSayi(yeni_gercek, yeni_sanal)  # Sonuç kompleks sayı olarak döner

    def __eq__(self, diger):  # Eşitlik kontrolü (==)
        return self.gercek == diger.gercek and self.sanal == diger.sanal  # Her iki kısım da eşitse True

    def __ne__(self, diger):  # Eşit değil (!=)
        return not self == diger  # Eşit değilse True

    def __lt__(self, diger):  # Küçüktür (<)
        return self.gercek + self.sanal < diger.gercek + diger.sanal  # Toplam değere göre karşılaştırma

    def __le__(self, diger):  # Küçük eşit (<=)
        return self.gercek + self.sanal <= diger.gercek + diger.sanal

    def __gt__(self, diger):  # Büyüktür (>)
        return self.gercek + self.sanal > diger.gercek + diger.sanal

    def __ge__(self, diger):  # Büyük eşit (>=)
        return self.gercek + self.sanal >= diger.gercek + diger.sanal

    def norm(self):  # Norm (uzunluk) |z| = √(a² + b²)
        return math.sqrt(self.gercek**2 + self.sanal**2)  # math.sqrt ile karekök alınır

    def birim(self):  # Birim vektör z / |z|
        n = self.norm()  # Norm (uzunluk) alınır
        return KompleksSayi(self.gercek / n, self.sanal / n)  # Her kısım norma bölünür

    def tersi(self):  # Karmaşık sayının tersi (1/z)
        payda = self.gercek**2 + self.sanal**2  # |z|² hesaplanır
        return KompleksSayi(self.gercek / payda, -self.sanal / payda)  # Gerçek kısım/payda, sanal kısmın işareti değişir

    def aci(self):  # Karmaşık sayının açısı (argümanı)
        if self.gercek == 0 and self.sanal == 0:  # 0 için açı tanımsızdır
            raise ValueError("Sıfır sayısında açı tanımsızdır")
        return math.atan2(self.sanal, self.gercek)  # atan2 fonksiyonu ile açı hesaplanır

# ReelSayi adında başka bir sınıf tanımlıyoruz, KompleksSayi'den kalıtım alıyor
class ReelSayi(KompleksSayi):
    def __init__(self, deger):  # Sadece reel kısım alır, sanal kısım 0 olur
        super().__init__(deger, 0)

    def karekok(self):  # Reel sayının karekökü
        if self.gercek < 0:  # Negatif sayının karekökü tanımsız
            raise ValueError("Negatif reel sayının karekökü tanımsızdır.")
        return math.sqrt(self.gercek)  # Kareköklü değer döndürülür

# Ana program burada başlıyor
if __name__ == "__main__":

    sayi1 = KompleksSayi(3, 4)  # 3 + 4i kompleks sayısı oluşturuluyor
    sayi2 = KompleksSayi(1, -2)  # 1 - 2i kompleks sayısı oluşturuluyor

    print("Sayı 1:", sayi1)  # sayi1 nesnesi yazdırılıyor (__str__ metodu çalışır)
    print("Sayı 2:", sayi2)  # sayi2 nesnesi yazdırılıyor

    print("Toplam:", sayi1 + sayi2)  # İki kompleks sayının toplamı
    print("Fark:", sayi1 - sayi2)    # Farkı
    print("Çarpım:", sayi1 * sayi2)  # Çarpımı
    print("Bölüm:", sayi1 / sayi2)   # Bölümü

    print("Sayı 1'in normu:", sayi1.norm())  # sayi1'in normu hesaplanır
    print("Sayı 1'in birimi:", sayi1.birim())  # sayi1 birim sayıya dönüştürülür
    print("Sayı 1'in tersi:", sayi1.tersi())  # sayi1'in tersi (1/z)
    print("Sayı 1'in açısı:", sayi1.aci())  # sayi1'in argümanı (radyan cinsinden)

    reel_sayi = ReelSayi(9)  # 9 değeriyle bir reel sayı nesnesi oluşturuluyor
    print("Reel sayı:", reel_sayi)  # Reel sayı yazdırılır
    print("Reel sayının karekökü:", reel_sayi.karekok())  # Karekökü hesaplanır

    print("Sayı 1 == Sayı 2 mi?", sayi1 == sayi2)  # Eşitlik karşılaştırması
    print("Sayı 1 < Sayı 2 mi?", sayi1 < sayi2)    # Küçüklük karşılaştırması
