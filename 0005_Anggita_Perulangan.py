

print ("Latihan")
print ("Buatlah bilangan ganjil dan bilangan genap dari 1 sampai 50 menggunakn perulangan")
print ("Bilangan Ganjil")
angka = 1
while angka <=50:
    if(angka == 1):
        print("Bilangan ganjil",angka)
    angka = angka + 2
    print("Bilangan ganjil",angka)
    if(angka==49):
        break

print ("\n")
print ("Bilangan Genap")
angka = 0
while angka<=50:
    if(angka ==0):
        print('Bilangan genap',angka)
    angka = angka + 2
    print('Bilangan genap',angka)
    if(angka==50):
        break

print ("\n")
print ("Buat program yang menampilkan semua bilangan prima antara 1 sampai 100 menggunakan perulangan")
for angka in range(2, 101):
    prima = True

    for pembagi in range(2, angka):
        if angka % pembagi == 0:
            prima = False
            break

    if prima:
        print(angka)
