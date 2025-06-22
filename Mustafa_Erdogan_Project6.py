import string  # Harf kümesi işlemleri için kullanılır (A-Z)

# Metni temizleyen fonksiyon
def clean_text(text):
    # Metni büyük harfe çevir ve sadece alfabetik karakterleri al
    return ''.join(c.upper() for c in text if c.isalpha())

# Caesar şifreleme fonksiyonu
def encrypt(text, k):
    result = ""
    for char in text:
        if char.isalpha():
            # Harfi A=0, B=1, ..., Z=25 şeklinde indeksle
            # k kadar kaydır ve tekrar A-Z karakterine dönüştür
            shifted = (ord(char) - ord('A') + k) % 26
            result += chr(shifted + ord('A'))
    return result

# Caesar şifre çözme fonksiyonu
def decrypt(text, k):
    result = ""
    for char in text:
        if char.isalpha():
            # Şifre çözmede k kadar geri kaydır
            shifted = (ord(char) - ord('A') - k) % 26
            result += chr(shifted + ord('A'))
    return result

# Harf frekans analizi yapan fonksiyon
def frequency_analysis(text):
    # A-Z harfleri için başlangıç frekansları sıfırla
    freq = {letter: 0 for letter in string.ascii_uppercase}
    for char in text:
        if char.isalpha():
            # Her harfi say
            freq[char] += 1
    return freq

# Ana fonksiyon: tüm işlemleri sırayla yapar
def main():
    # Öğrenci numarasını kullanıcıdan al
    student_number = input("Öğrenci numaranızı girin: ")
    
    # Son iki rakamı al ve 26'ya göre mod alarak şifreleme anahtarını (k) belirle
    k = int(student_number[-2:]) % 26
    
    # Eğer mod 26 sonucu 0 ise k=9 olarak sabitle
    if k == 0:
        k = 9

    # Girdi metnini input.txt dosyasından oku
    try:
        with open('input.txt', 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print("Hata: input.txt dosyası bulunamadı!")
        return

    # Metni temizle (sadece büyük harfli A-Z karakterleri kalsın)
    cleaned_text = clean_text(text)

    # Metni şifrele (encrypt)
    encrypted_text = encrypt(cleaned_text, k)

    # Şifrelenmiş metni plain_enc.txt dosyasına yaz
    with open('plain_enc.txt', 'w', encoding='utf-8') as file:
        file.write(encrypted_text)

    # Şifreyi çöz (decrypt)
    decrypted_text = decrypt(encrypted_text, k)

    # Çözülmüş metni plain_dec.txt dosyasına yaz
    with open('plain_dec.txt', 'w', encoding='utf-8') as file:
        file.write(decrypted_text)

    # Frekans analizini yap ve ekrana yazdır
    freq = frequency_analysis(decrypted_text)
    print("\nFrekans Analizi:")
    for letter in string.ascii_uppercase:
        print(f"{letter} harfi {freq[letter]} kere kullanılmıştır.")

# Program buradan başlar
if __name__ == "__main__":
    main()
