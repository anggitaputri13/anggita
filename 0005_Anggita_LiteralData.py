#Nama Variabel
nama = "Anggita Putri Rahayu"
print("Nama :", nama) 
umur = 19 
print("Umur :", umur, "Th")
berat = 46.6 
print("Berat :", berat,"Kg") 
print("\n")
#Ubah Tipe Data
angka_string = "123"
angka_float = 45.67 
angka_integer = 89 
print("\n")
#Konversi angka_string menjadi integer
angka_integer1 = int(angka_string) 
print("Angka = ", angka_integer1, ",type", type(angka_integer1))
#Konversi angka_float menjadi integer  
angka_integer2 = int(angka_float) 
print("Angka = ", angka_float, ",type", type(angka_float))
#Konversi angka_integer menjadi float 
angka_float = float(angka_integer) 
print("Angka = ", angka_float, ",type", type(angka_float))
#Konversi angka_integer menjadi string
angka_string = str(angka_integer) 
print("Angka = ", angka_string, ",type", type(angka_string))
print("\n")

#Program Input
Usia = int(input("Masukkan Usia: "))
print("Data", Usia,",type=", type(Usia))
Tinggi_Badan = float(input("Masukkan Tinggi Badan: "))
print("Data", Tinggi_Badan, ",type= ", type(Tinggi_Badan))
Nama = str(input("Masukkan Nama: "))
print("Data", Nama, ",type=", type(Nama))



