import random #rando sayılar verir 
from IPython.display import clear_output #clear output Jupyter Notebook veya terminalde eski çıktıyı temizleyip sadece yeni durumu göstermek için kullanılır.

# Karıştırma fonksiyonu (shuffle kullanmadan)
def my_shuffle(lst): 
    for i in range(len(lst) - 1, 0, -1): #listenin sonundan başlayarak başa doğru gideriz   x
        j = random.randint(0, i) #sıfır ila 1 arasından sayı seçeriz 
        lst[i], lst[j] = lst[j], lst[i] #seçilen rastgele elemanla mevcut elemanın yerini değiştirirz 
 
# Listeyi 3x3 matris şeklinde bastırma
def print_board(board): #o anki dokuz elemanlı listeyi temsil eder 
    for i in range(0, 9, 3): 
        print(board[i], board[i+1], board[i+2]) #her satırda 3 elemanı yan yana yazdırır 
    print()#amaç 3x3 matris şeklinde ekrena yazılmalı

# Boşluğun indeksini bul
def find_space(board):
    return board.index(" ") #boşluğun yerini tayin etmek için kullandık

# Taşıma fonksiyonu, yapılan hareketi de geri döndürür
def move(board, direction): #haraket fonksiyonumuz 
    idx = find_space(board) #boşluğun yeri 
    if direction == "w" and idx not in [0, 1, 2]:  # Yukarı
        board[idx], board[idx-3] = board[idx-3], board[idx]
        return "Yukarı hareket (w)"
    elif direction == "s" and idx not in [6, 7, 8]:  # Aşağı
        board[idx], board[idx+3] = board[idx+3], board[idx]
        return "Aşağı hareket (s)"
    elif direction == "a" and idx not in [0, 3, 6]:  # Sola
        board[idx], board[idx-1] = board[idx-1], board[idx]
        return "Sola hareket (a)"
    elif direction == "d" and idx not in [2, 5, 8]:  # Sağa
        board[idx], board[idx+1] = board[idx+1], board[idx]
        return "Sağa hareket (d)"
    else:
        return "Geçersiz hareket!"

# Çözülmüş hali kontrol et
def is_solved(board): #çözülmüş formu böyle olmalı
    return board == [1, 2, 3, 4, 5, 6, 7, 8, " "]

# Ana oyun döngüsü
def play_game():
    board = [1, 2, 3, 4, 5, 6, 7, 8, " "]
    my_shuffle(board)
    while is_solved(board):  # Eğer ilk karışık hali çözümlüyse tekrar karıştır
        my_shuffle(board)
                          
                          #KODUMUZ
    while True:
        clear_output(wait=True)
        print_board(board)
        if is_solved(board):
            print("Tebrikler puzzle çözüldü!")
            break
        move_input = input("Hareket (w: yukarı, a: sola, s: aşağı, d: sağ): ")
        if move_input in ["w", "a", "s", "d"]:
            result = move(board, move_input)
            clear_output(wait=True)
            print(result)
            print_board(board)
        else:
            print("Geçerli bir tuş giriniz (w, a, s, d).")

play_game()