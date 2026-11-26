# Program 12.1 Pengenalan Fungsi
## --- MEMBUAT FUNGSI --- 
def hello_world(): # menampilkan hello world , Fungsinya
    print("hello world")       
    print("Kepada Fauzan Zein") 
    print("Dan juga kepada Faza Biri Biri") 
hello_world()  # pemanggilnya


# Program 12.2 Fungsi dengan Argumen
## --- Fungsi dengan argumen ---  
## def nama_fungsi(argumen)
 #      Badan fungsi  
def hello_world(nama):   #fungsi hello world menerima   
   print(f"Selamat datang di Dunia, {nama}")
   hello_world("ucup")  
   
def tambah(angka_1, angka_2):   # fungsi tambah   
    hasil = angka_1 + angka_2   
    print(f"{angka_1} + {angka_2} = {hasil}")  
tambah(1,8)   #jangan di Tab 

def say_hi(list_peserta):   #fungsi say hi   
    data_peserta = list_peserta.copy()   
    for peserta in data_peserta:     
        print(f"Selamat datang {peserta}")  
kumpulan_mahasiswa = ["Budi", "Tono", "Joko"]  
say_hi(kumpulan_mahasiswa)

#Program 12.3 Fungsi dengan return
# template fungsi kembalian 
# def nama_fungsi(argumen): 
#      badan fungsi 
#      return output  
#  fungsi kuadrat
def kuadrat(input_angka):   
    output_kuadrat = input_angka ** 2   
    return output_kuadrat
y = kuadrat(5) 
print(y)  

print(kuadrat(6))  

z = 10 + kuadrat(7) 
print(z)

def fungsi_tambah(angka_1, angka_2):   # fungsi return dengan multi input   
    return angka_1 + angka_2  
a = fungsi_tambah(10, 8) 
print(a)  

def operasi_matematika(angka_1, angka_2):
    tambah = angka_1 + angka_2   
    kurang = angka_1 - angka_2   
    kali = angka_1 * angka_2   
    bagi = angka_1 / angka_2    
    return tambah,kurang,kali,bagi  
k,l,m,n = operasi_matematika(9,5)  
print(f"Hasil tambah = {k}") 
print(f"Hasil kurang = {l}") 
print(f"Hasil kali = {m}") 
print(f"Hasil bagi = {n}") 

#Program 12.4 Default Argumen Fungsi 
# Default argument  
# # def fungsi(argument): 
# # def fungsi(argument = nilai default):  
# # contoh 1 
def say_hello(nama = "Ojul"):   
    print(f"Hello {nama}")  
    say_hello("Ucup") 
    say_hello() 

# contoh 2 
def sapa_dia(nama, pesan = "Apa kabar?"):   # fungsi dengan satu input biasa, dan satu default arg   
    print(f"hai {nama}, {pesan}")  
    sapa_dia("Nanda","Selamat pagi") 
    sapa_dia("Budi")

# contoh 3 
def hitung_pangkat(angka, pangkat):   
    hasil = angka**pangkat   
    return hasil  
print(hitung_pangkat(2,4))  
hasil = hitung_pangkat(pangkat=3, angka=5) 
print(hasil) 

# contoh 4 
def faktorial(input_1=1,input_2=2,input_3=3,input_4=4):   
    hasil = input_1 * input_2 * input_3 * input_4   
    return hasil  
print(faktorial()) 
print(faktorial(input_3 = 10))

print("\n")
print ("LATIHAN")
print("Buatlah program dengan input dan fungsi untuk menghitung: ")
print("a. Luas persegi panjang ")

def luasPersegiPanjang (panjang, lebar):
    luas2 = panjang * lebar
    return luas2

p = int(input("panjang ="))
l = int(input("lebar ="))

hasil_luas = luasPersegiPanjang(p,l)
print("Luas persegi panjang = ", hasil_luas)    #memanggil fungsinya

print("b. Volume persegi panjang")

def VolumePersegiPanjang (panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi 
    return volume

p = int(input("panjang ="))
l = int(input("lebar ="))
t = int(input("tinggi ="))

hasil_volume = VolumePersegiPanjang(p,l,t)
print("Volume persegi panjang = ", hasil_volume)

print("c. Luas lingkaran ")

def LuasLingkaran (jari_jari) :
    return 3.14 * jari_jari ** 2

r = float(input("jari jari ="))

print ("Luas lingkaran = ", LuasLingkaran(r))

print("d. Volume bola")

def VolumeBola (jari_jari2):
    return 4/3 * 3.14 * jari_jari2 **3

r = float(input("jari jari ="))

print ("Volume Bola =", VolumeBola(r))