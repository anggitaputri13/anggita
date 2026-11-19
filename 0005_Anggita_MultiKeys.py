# Program 11.1 Multi keys & Nesting Dictionary

import datetime
mahasiswa1 = {
    "nama" : "Ucup Markucup",
    "NPM" : "198789009",
    "sks_lulus" : 112,
    "Beasiswa" : False,
    "Lahir" : datetime.datetime(2001, 2, 10) #tahun, tanggal, bulan
}

mahasiswa2 = {
     "nama" : "Siti Markonah",
     "NPM" : "198789010",
     "sks_lulus" : 122,
     "Beasiswa" : True,
     "Lahir" : datetime.datetime(2002, 5, 3) #tahun, tanggal, bulan
}

mahasiswa3 ={
     "nama" : "Yanto Yantii ",
     "NPM" : "198789011",
     "sks_lulus" : 135,
     "Beasiswa" : False,
     "Lahir" : datetime.datetime(2003, 2, 7) #tahun, tanggal, bulan
}
data_mahasiswa = {  
    'MAH001':mahasiswa1,  
    'MAH002':mahasiswa2,  
    'MAH003':mahasiswa3, } 

print(data_mahasiswa["MAH002"])

print("\n")

#kita akan membuat data tersebut agar lebih rapi seperti database

print(f"{"KEY":<7} | {"Nama":<16} | {"SKS":<8} | {"Beasiswa":<12} | {"Lahir":<40}") 
print("-"*76) 

for key, mhs in data_mahasiswa.items():
    format_lahir = mhs['Lahir'].strftime("tanggal %d bulan %m tahun %y")
    print(f"{key:<6}: | {mhs['nama']:<16} | {mhs['sks_lulus']:<8} | {str(mhs['Beasiswa']):<12} | {format_lahir:<40}")

print ("\n")

# Program 11.2 Latihan Dictionary Bagian 1

data_mahasiswa = {}

while True:
    mahasiswa = {}

    nama = input("Nama: ")
    jenis_kelamin = input("Jenis kelamin: ")
    npm = int(input("NPM: "))

    mahasiswa["nama"] = nama
    mahasiswa["jenis_kelamin"] = jenis_kelamin

    print(mahasiswa)

    # Simpan ke data mahasiswa
    data_mahasiswa[npm] = mahasiswa

    lagi = input("Tambah lagi (y/n)? ")
    if lagi == "n":
        break

print("Selesai")
# Tampilkan semua data Mahasiswa
print(data_mahasiswa)


    # Program 11.3 Latihan Dictionary Bagian 2 
     
print("\n")

import datetime
import os
import string
import random
mahasiswa_template = {
    'nama' : 'nama',
    'nim' : '00000000',
    'sks_lulus' : 0,
    'lahir' : datetime.datetime(1111,1,11)
}

data_mahasiswa1 = {}
while True:
    os.system
    mahasiswa1 = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa1['nama'] = input('Nama Mahasiswa:')
    mahasiswa1['nim'] = input('NIM Mahasiswa:')
    mahasiswa1['sks_lulus'] = int(input('SKS Lulus:'))
    thn_lahir = int(input('Tahun Lahir (YYYY):'))
    bln_lahir = int(input('Bulan Lahir (1-12):'))
    tgl_lahir = int(input('Tanggal Lair (1-31):'))
    mahasiswa1['lahir'] = datetime.datetime (thn_lahir,bln_lahir,tgl_lahir)
    print(mahasiswa1)

    KEY = ''.join(random.choice(string.ascii_uppercase) for i in range (6))  
    data_mahasiswa1.update({KEY:mahasiswa1}) #update untuk menambahkan data
    
    print(f"{"KEY":<7} | {"Nama":<16} | {"SKS":<8} | {"Lahir":<40}") 
    print("-"*76) 

    for mahasiswa in data_mahasiswa1 :
            KEY = mahasiswa

            NAMA = data_mahasiswa1[KEY]['nama']
            NIM = data_mahasiswa1[KEY]['nim']
            SKS = data_mahasiswa1[KEY]['sks_lulus']
            LAHIR = data_mahasiswa1[KEY]['lahir'].strftime("%x")

            print(f"{KEY:<6}: | {NAMA:<16} | {SKS:<8} | {LAHIR:<40}")

    print("\n")
    is_done = input("Lanjut Program? (y/n)")
    if is_done == "n" : #Sesuaikan kondisi selesai
        break

    print("Akhir dari program, terima kasih")
