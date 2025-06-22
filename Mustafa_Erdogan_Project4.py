def alt_matrisi_olustur(m, satir, sutun):
    return [ [m[i][j] for j in range(len(m)) if j != sutun] for i in range(len(m)) if i != satir ]

def determinant(m): 
    if len(m) == 1:
        return m[0][0]
    if len(m) == 2:
     return m[0][0]*m[1][1] - m[0][1]*m[1][0]
    
    det = 0
    for j in range(len(m)):
        alt_m = alt_matrisi_olustur(m, 0, j)
        det += ((-1) ** j) * m[0][j] * determinant(alt_m)
    return det

def matris_al(): #burada matris boyutunu ayarlayacagimiz fonksiyon 
    while True:
        try:
            boyut = int(input("Matrisin boyutunu (pozitif tam sayı) girin: "))
            if boyut <= 0:
                print("Pozitif tam sayı girmelisiniz.")
                continue
            break
        except ValueError:
            print("Geçerli bir sayı giriniz.") #eğer negatif bir boyut girilir ise program hata verecek

    matris = []
    for i in range(boyut):
        satir = []
        for j in range(boyut):
            while True:
                try:
                    eleman = int(input(f"{i+1}. satır {j+1}. sütun elemanını girin: "))
                    satir.append(eleman)
                    break
                except ValueError:
                    print("Geçerli bir tam sayı giriniz.")
        matris.append(satir)

    return matris

# Anaprogram
matris = matris_al()
print("Girilen matris:")
for satir in matris:
    print(satir)

det = determinant(matris)
print("Matrisin determinantı:", det)
