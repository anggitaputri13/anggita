# #--- LIST ---
# # Kumpulan data numbers 
data_angka = [1,5,2,3] 
print(data_angka) 
print("\n")
# # Kumpulan data_string 
data_string = ["ucup","adit","siti"] 
print(data_string)
print("\n")
# # Kumpulan data boolean 
data_boolean = [True, False, True, True] 
print(data_boolean) 
print("\n")
# # Kumpulan campuran 
data_campuran = [1,"bakwan",2,"cireng","ucup",True,"adit",False] 
print(data_campuran) 
print("\n")
# # Cara alternatif membuat list
data_range = range(0,10,2) # range(start,stop,step) 
print(data_range) 
print("\n")
data_list = list(data_range) 
print(data_list) 

print("\n")

# # --- Operasi LIST ---
data1 = range(0, 10, 3) #star, stop, step
print(data1)
print("\n")
data_list1 = list(data1)
print(data_list1)
print("\n")

# print("Manipulasi")

data2 = ["Bambang", "Ucup", "Asep"]
# #           0         1       2    lebih gampang jika akan mencetak data dari awal
# #           -3       -2      -1    lebih gampang jika akan mencetak data dari akhir
print(data2[0])
print("\n")
# data = ["Bambang", "Ucup", "Asep"]
# #           0         1       2
data_2 = data2[2]
print(data_2)
print("\n")
banyak_data = len(data2)
print(banyak_data)
print("\n")
# print("Menambahkan Data")
# # insert (posisi, item)
data2.insert(1, "Joko")      #menyesuaikan tempat
print(data2)
print("\n")
data2.append("Izuddin")      #diletakan dipaling atas
print(data2)
print("\n")
# # menambahkan list
bajak_laut = ["luffy", "Zoro", "Nami"]
data2.extend(bajak_laut)
print(data2)
print("\n")

print("-------Tugas--------")
print("====================")
#1. Diberikan list berikut: 
kendaraan = ['motor', 'mobil', 'sepeda', 'bus'] 
#               0        1         2       3
# a. Tambahkan 'truk' di akhir list 
kendaraan.append("truk")
print(kendaraan)
print("\n")
# b. Sisipkan becak' pada index ke-1 
kendaraan.insert(1, 'becak')
print(kendaraan)
print("\n")
# c. Hapus data yang berada paling belakang dari list tersebut
kendaraan.pop()
print(kendaraan)
print("\n")
# d. Ubah elemen 'sepeda' menjadi 'skuter'
# ['motor', 'becak', 'mobil', 'sepeda', 'bus']
#     0        1        2         3       4  
kendaraan [3] = "skuter"
print(kendaraan)
print("\n")
# e. Tampilkan informasi jumlah total data di dalam list tersebut
banyak_data = len(kendaraan)
print(banyak_data)
print("\n")

# 2. Diberikan list berikut: 
angka = [75, 80, 90, 75, 85, 100, 65]

# a. Cari tahu di indeks ke berapa skor 100 berada
index_100 = angka.index(100)
print (f"index 100 berada pada = {index_100}")
print("\n")
# b. Hitung ada berapa banyak siswa yang mendapatkan skor 75
skor75 = angka.count(75)
print (f"banyak siswa yang mendapatkan skor 75 = {skor75}")
print("\n")
# c. Urutkan list skor_ujian tersebut dari nilai terkecil hingga terbesar
angka.sort()
print(f"urutkan nilai dari yang terendah = {angka}")
print("\n")
# d. Balikkan urutan list yang sudah diurutkan tersebut sehingga menjadi dari terbesar ke terkecil. 
angka.reverse()
print(f"urutan list dari yang terbesar = {angka}")
print("\n")

# 3. Gabungkan menu_tambahan ke dalam menu_utama menggunakan fungsi,
#    kemudian tampilkan hasil dari data gabungan tersebut. 
menu_utama = ["Nasi Goreng", "Mie Ayam"] 
menu_tambahan = ["Kerupuk", "Es Teh"]
nested_list = [menu_utama, menu_tambahan]
print(nested_list)
print("\n")

# 4. Diberikan data nested list berupa informasi nama barang dan harganya:
data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]

# a. Tampilkan harga dari "Pensil" (yaitu 2000) dengan memanggil indeks baris 
#    dan kolom yang spesifik dari list tersebut.

print (f"informasi barang {data_barang [1]}")

# b. Gunakan perulangan untuk membaca data satu per satu, lalu tampilkan output dengan format:
#    "Nama: [nama barang], Harga: [harga]" untuk setiap elemen di dalamnya. 

for barang in data_barang:
    print (f"Nama Barang\t : {data_barang [0]} ")
    print (f"Harga\t : {data_barang[1]}\n")