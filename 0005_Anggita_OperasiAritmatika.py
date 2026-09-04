#Program 3.1 Menampillkan output dari operasi sederhana
print("Operasi Aritmatika")
a = 12
b = 6
# operasi penjumlahan (+)
hasil = a + b 
print(a,"+",b,"=",hasil) 
# operasi pengurangan (-)
hasil = a - b 
print(a,"-",b,"=",hasil) 
# operasi perkalian (*)
hasil = a * b 
print(a,"*",b,"=",hasil)
# operasi pembagian (/)
hasil = a / b 
print(a,"/",b,"=",hasil)
# operasi eksponen atau pangkat (**)
hasil = a ** b 
print(a,"**",b,"=",hasil)
# operasi modulus (%)
hasil = a % b 
print(a,"%",b,"=",hasil)
# operasi floor division (//)
hasil = a // b 
print(a,"//",b,"=",hasil)

# Program 3.2 konversi celcius ke satuan lain
print("PROGRAM KONVERSI TEMPERATUR")
# program konversi celcius ke satuan lain 
celcius = float(input("Masukan suhu dalam celcius : ")) 
print("suhu adalah", celcius, "Celcius") 
# reamur 
reamur = (4/5) * celcius 
print("Suhu dalam reamur adalah" , reamur, "Reamur") 
# fahrenheit 
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah ", fahrenheit, "Fahrenheit") 
# kelvin 
kelvin = celcius + 273 
print("Suhu dalam kelvin adalah ", kelvin, "Kelvin") 

#Program 3.3  Operasi komperasi 
# setiap hasil dari operasi komperasi adalah boolean   
# # >,<,>=,<=,==,!=,is,is not 
a = 8
b = 2 
# lebih besar dari > 
print("=============== lebih besar dari (>)")
hasil = a > 3 
print(a,">",b,"=",hasil)
hasil = b > 3 
print(b,">",3,"=",hasil)
hasil = b > 5 
print(b,">",5,"=",hasil)
# kurang dari < 
print("=============== kurang dari (<)") 
hasil = a < 3 
print(a,"<",b,"=",hasil) 
hasil = b < 3
print(b,"<",3,"=",hasil) 
hasil = b < 7
print(b,"<",7,"=",hasil) 
# lebih dari sama dengan >= 
print("=============== lebih dari sama dengan (>=)") 
hasil = a >= 3 
print(a,">=",b,"=",hasil)
hasil = b >= 3 
print(b,">=",3,"=",hasil)
hasil = b >= 5 
print(b,">=",5,"=",hasil)
# kurang dari sama dengan <= 
print("=============== kurang dari sama dengan (<=)") 
hasil = a <= 3 
print(a,"<=",b,"=",hasil) 
hasil = b <= 3
print(b,"<=",3,"=",hasil) 
hasil = b <= 7
print(b,"<=",7,"=",hasil) 
#sama dengan (==) 
print("=============== sama dengan (==)")
hasil = a == 8
print(a,"==",8,"=",hasil) 
hasil = b == 8
print(b,"==",8,"=",hasil) 
# tidak sama dengan (!=) 
print("=============== sama dengan (!=)") 
hasil = a != 8
print(a,"!=",8,"=",hasil) 
hasil = b != 8
print(b,"!=",8,"=",hasil) 

#PENUGASAN
#sebuah bangunan dengan nilai
Panjang = 12 
Lebar = 5 
Tinggi = 8
print("\n")
# a. Hitunglah luas, volume dan keliling dari bangunan tersebut! 
#Menghitung Luas Balok
Luas = 2*((Panjang*Lebar) + (Panjang*Tinggi) + (Lebar*Tinggi))
print("Luas =" ,Luas)
#Menghitung Volume Balok
Volume = Panjang * Lebar * Tinggi
print("Volume =", Volume)
#Menghitung Keliling Balok
Keliling = 4*(Panjang + Lebar + Tinggi)
print("Keliling =" ,Keliling)
# b. Apakah luas bangunan tersebut lebih luas dari 50? 
hasil = Luas > 50 
print(Luas,">",50,"=",hasil)
# Apakah volume tersebut bernilai 480? 
hasil = Volume == 480
print(Volume,"==",480,"=",hasil) 
