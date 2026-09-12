#Latihan 
# 1. Buatlah program yang meminta user memasukkan usia seseorang, lalu kategorikan usia tersebut berdasarkan kriteria berikut: 
# • 0 - 12 tahun: Anak-anak 
# • 13 - 17 tahun: Remaja 
# • 18 - 59 tahun: Dewasa 
# • 60 tahun ke atas: lansia 

print("Latihan ")

usia = int(input("Masukkan Usia: "))

if usia <= 12:
    print("Anak anak")
elif usia <= 17:
    print("Remaja")
elif usia <= 59:
    print("Dewasa")
else:
    print("Lansia")
