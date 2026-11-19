import datetime #Berfungsi untuk mengelola dan memformat data tanggal serta waktu
import random #Berfungsi untuk memilih atau menghasilkan data secara cak (digunakan untuk membuat KEYS acak)
import string #Berfungsi untuk menyediakan kumpulan karakter huruf (A-Z) yang akan diacak

#Membuat template dasar (kamus kosong )
buku_template = {
    'judul':'',
    'penulis':'',
    'tahun_terbit': 0,
    'tanggal_pinjam':datetime.datetime(1111,1,11),  #tahun, bulan, tangggal
    'status':''
}

data_perpustakaan = {}

#Memulai perulangan agar program bisa terus berjalan dan meminta input berulang-ulang menggunakan (while True)
while True:
    print("\n Sistem Manajemen Perpustakaan ")
    buku = dict.fromkeys(buku_template.keys())         #dict.fromkeys dgnkan untuk menyalin, mebuat, atau menduplikasi struktur keys

    #Mengambil input data teks (judul, penulis, dll) dari pengguna melalui terminal
    buku['judul'] = input("Judul Buku:")
    buku['penulis'] = input("Penulis:")
    buku['tahun_terbit'] = int(input("Tahun Terbit:"))

    #Mengambil input komponen tanggal terakhir pinjam satu per satu dari pengguna
    tahun = int(input('Tahun Terakir Pinjam (YYYY):'))
    bulan = int(input('Bulan Terakir Pinjam (1-12):'))
    tanggal = int(input('Tanggal Terakir Pinjam (1-31):'))

    #Menggabungkan komponen tahun, bulan, tanggal ke dalam format objek datetime
    buku['tanggal_pinjam'] = datetime.datetime(tahun, bulan, tanggal)
    buku['status'] = input('Status (Tersedia/Tidak Tersedia):')

    #Membuat Keys unik secara otomatis berupa gabungan 6 huruf kapital acak
    KEY = ''.join((random.choice(string.ascii_uppercase)for i in range(6)))

    #Memasukkan data buku yang baru diinput ke dalam dictionary utama 'data_perpustakaan' 
    data_perpustakaan.update({KEY:buku})
    print(f"{'KEYS':<8} {'JUDULBUKU':<18} {'PENULIS':<14} {'TAHUN':<6} {'TGL PINJAM':<12} {'STATUS':<10}")
    print("-"*80)

    #Melakukan perulangan untuk membaca dan mencetak setiap data buku yang ad adi dalam database
    for key, b in data_perpustakaan.items():
        #Mengubah format objek datetime tanggal pinjam menjadi teks berformat DD-MM-YYYY agar mudah dibaca
        format_tgl = b['tanggal_pinjam'].strftime('%d-%m-%Y')
        print(f'{key:<8} {b['judul']:<8} {b['penulis']:<14} {b['tahun_terbit']:<6} {format_tgl:<12} {b['status']:<10}')

    print('\n')
    #Menanyakan kepada pengguana apakah ingin menghentikan program atau lanjut memnambah data
    is_done = input('Apakah kamu mau menambahkan buku lagi? (y/n):')

    #Jika pengguna mengetik 'n', maka perulangan while True akan dihentikan 
    if is_done.lower() == "n":
        break

#Pesan penutup yang akan muncul setelah perulangan selesai atau dihentikan
print('\nAkhir dari program, terima kasih')