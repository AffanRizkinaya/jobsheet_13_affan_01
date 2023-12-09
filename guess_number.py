# Membuat Game Guessing
def guess_number():
    angka_rahasia = 9
    batas = 3
    penghitung = 1

    print ("!!Quiz tebak angka!!")
    while True:
        user = int(input("Masukkan angka : "))
        if user == angka_rahasia:
            print("Selamat Jawaban Anda Benar!")
            break
        elif penghitung == batas:
            print("Maaf anda Gagal")
            break
        elif user != angka_rahasia:
            print("Coba Lagi!")
            penghitung += 1
