#Tuples
#yang membedakan dengan list adalah bagian kurung nya 
data_tuples = (1,2,3,4,5)
print(data_tuples)
#untuk menampilkan index ke 3
print(data_tuples[3])
#untuk menambahkan data


#set (Himpunan)
#menggunakan kurung kurawal 
#tidak ada dupllikasi
data_sets = {10, 4, 3, 2}
print(data_sets)
print("\n")
data_sets2 = {10, 4, 3, 2, 3, 8}
print(data_sets2)

#distionary
data_mahasiswa1 = ["Ucup", 260506, "sastra mesin", "79", "P", "Rombel 1"]
data_manusia ={
    "Nama": "Ucup", 
    "NPM" : 260506,
    "Prodi" : "Sastra mesin",
    "JK"  : "Pria",
    "Rombel" : "Rombel 1",
}
print(data_manusia["Nama"])  #memanggilnnya menngunakan Key, bukan index

#cara mengecek KEY dari data manusia
KEY = "hewan"
CHECKKEY = KEY in data_manusia
print(CHECKKEY)

#cara mengubah data pada KEY
data_manusia["Nama"] = "Bambang"
print(data_manusia["Nama"])

data_manusia["Hewan"] = "Sapi"
print(data_manusia)

#cara menghapus data
del data_manusia["JK"]
print(data_manusia)

#Looping Distionary
data_mahasiswa2 ={
    "nama" : "Siti",
    "umur" : 12,
    "JK"   : "Pria",
    "BB"   : 38,
    "TB"   : 98,
}

# for inisialisasi in dis     akan menampilkan KEY nya
for mahasiswa2 in data_mahasiswa2:
    print(mahasiswa2)

for mahasiswa2 in data_mahasiswa2.values():  #akan menampilkan datanya
    print(mahasiswa2)

for mahasiswa2 in data_mahasiswa2.items():   #akan menampilkan KEY dan datanya
    print(mahasiswa2)

for key, value in data_mahasiswa2.items():
    print(f"Key nya adalah {key}, value nya adalah {value}")   #f biar bisa nampilin berbagai tipe data

print("\n")
print("========TUGAS========")
#Nomer 1 Tuple
#a. Buatlah sebuah Tuple bernama mahasiswa yang berisi 3 data diri Anda: ("Nama", "NIM", "Prodi").
data_mahasiswa = ("Anggita Putri Rahayu", 2605060005, "Teknologi Informasi")
#b. Tampilkan data NIM dan Prodi ke layar dengan cara mengakses indeksnya. 
print("NIM:", data_mahasiswa[1])
print("Prodi:", data_mahasiswa[2])

#c. Coba jalankan kode mahasiswa[2] = "Teknologi Informasi". 
# Amati pesan error yang muncul, lalu jelaskan mengapa hal tersebut terjadi 
#data_mahasiswa[2] = "Teknologi Informasi"

#print("Tuple bersifat immutable (tidak dapat diubah setelah didefinisikan). " \
#"Kita tidak bisa menambah, mengubah, atau menghapus elemen di dalam tuple secara langsung setelah tuple tersebut dibuat.")

#d. Buatlah sebuah Set bernama nilai_angka dari barisan angka berikut: 10, 4, 3, 2, 4, 10, 7, 5. 
# Cetak nilai_angka ke layar dan jelaskan apa yang terjadi pada angka 10 dan 4 yang ditulis dua kali! 
nila_angka = 10, 4, 3,2 ,4 ,10,7,5   #data sets
print(nila_angka)
# Berbeda dengan list atau tuple, Set tidak menyimpan elemen duplikat (ganda). Oleh karena itu,
#  angka 10 dan 4 yang ditulis dua kali akan otomatis disaring sehingga masing-masing hanya akan muncul satu kali di dalam hasil cetak set.

#Nomer 2 Manipulasi Dictionary 
#a. Buatlah sebuah dictionary bernama data_mahasiswa dengan pasangan key-value berikut: 
data_mahasiswa_untidar={
    "NPM": 2605060005,
    "Nama" : "Anggita Putri Rahayu",
    "Prodi" : "Teknologi Informasi",
}
for key, value in data_mahasiswa_untidar.items():
    print(f"{key}: {value}")

#b. Ubah nilai "prodi" menjadi "Sastra Mesin " sekaligus menambahkan key baru "angkatan" dengan nilai 2026. 
data_mahasiswa_untidar["Prodi"] = "Sastra Mesin"
data_mahasiswa_untidar["Angkatan"] = 2026
print(data_mahasiswa_untidar)

#c. Hapus data "nim", lalu tampilkan hasil akhir dictionary ke layar. 
del data_mahasiswa_untidar ["NPM"]
print(data_mahasiswa_untidar)

#nomer 3
#3. Perulangan pada Dictionary 
#a. Buatlah dictionary bernama keranjang dengan data harga buah berikut: 
# {"apel": 5000, "pisang": 3000, "jeruk": 7000, "anggur": 15000} 
keranjang = {
    "Apel" : 5000,
    "Pisang" : 3000,
    "Jeruk" : 7000,
    "Anggur" : 15000,
}

#b. Gunakan perulangan untuk menampilkan setiap barang dan harganya 
# dengan format: "Harga apel: Rp 5000" 
total_belanja = 0
for barang, harga in keranjang.items():
    print(f"Harga {barang}, = Rp. {harga}")

#c. Tampilkan total belanja 
    total_belanja += harga

# Menampilkan hasil total belanja di luar perulangan
print(f"\nTotal belanja: Rp {total_belanja}")


