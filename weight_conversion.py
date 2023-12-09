# Program konversi berat
def weight_conversion():
    print ("!!Program konversi berat!!")
    while True:
        berat = float(input("Masukkan berat : "))
        tipe = input("Lbs(L) atau Kg(K) : ")
        if tipe == 'L' or tipe == 'l':
            konversi1 = berat * 2.204623
            print(f"{berat} kg = {konversi1:.2f} pound")
            break
        elif tipe == 'K' or tipe == 'k':
            konversi2 = berat * 0.453592
            print(f"{berat} pound = {konversi2:.2f} kg")
            break