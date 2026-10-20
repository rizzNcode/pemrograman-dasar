# Soal 1
nama = "Rizki"
umur = 20
tinggiBadan = 169.4

print(f"Hallo nama saya {nama}, umur saya {umur}, tinggi badan saya adalah {tinggiBadan}")

# Soal 2
a = 17
b = 5

print(a+b, a-b, a*b, a/b, a%b )
print(a//b) #merupakan hasil pembagian yang pembulatan kabawah, tidak berbentuk desimal

# Soal 3
x = 10
y = 20

temp = x
x = y
y = temp 
print(x,y)

# Soal 4
angka = int (input("Masukkan angka : "))

if angka % 2 == 0:
    print(f"{angka} adalah bilangan genap")
else :
    print(f"{angka} adalah bilangan ganjil")    

# Soal 5
nilai = int(input("Masukkan Nilai :"))

if nilai >=60 :
    print ("Anda Lulus")
else :
    print ("Anda Tidak Lulus")    

# Soal 6
usia = int(input("Usia Minimal untuk membuat KTP :"))

if usia >=17 :
    print ("Boleh membuat KTP")
else :
    print ("Belum boleh membuat KTP")    

# Soal 7
bil1 = int(input("Masukan bilangan 1 :"))    
bil2 = int(input("Masukan bilangan 2 :"))    

if bil1 > bil2 :
    print(f"{bil1} lebih besar dari {bil2}")
elif bil1 == bil2 :
    print (f"{bil1} sama besar dengan {bil2}")
else :
    print(f"{bil2} lebih besar dari {bil1}")    

# Soal 8
angka3 = int (input("Masukkan soal kelipatan angka 3 :"))

if angka3 % 3 == 0 :
    print ("Habis dibagi 3")
else :
    print ("Tidak habis dibagi 3")    

# Soal 9 
total = int (input("Masukkan Total Belanja :"))
diskon = 10


if total >= 100000 :
    potongan = total * (diskon / 100)
    setelahDiskon = total - potongan
    print (f"Total Harga awal adalah {total}, Anda mendapat potongan sebesar {diskon}%, jadi total Belanja anda sekaranag adalah {setelahDiskon}")
else :
    print (f"Total Harga adalah {total}")  

# Soal 11 
nilai11 = int(input("Masukkan Nilai : "))

if nilai11 >= 85 :
    print ("A")
elif nilai11 >= 70 and nilai11 <= 84:
    print ("B")    
elif nilai11 >= 60 and nilai11 <= 69:
    print ("C")    
else :
    print ("D")

#Tahun Kabisat
tahun  = int(input("Cek tahun kabisat :"))

if (tahun  % 4 == 0 and tahun % 100 != 0) or tahun % 400 == 0 :
    print ("Kabisat")
else :
    print ("Bukan Kabisat")    

# Dikon Usia 
# hargaDasar = 50000
# diskon = 50
# usia = int(input("Masukkan Usia"))

# if usia < 12 or usia > 60 :
#     hargaAkhir = hargaDasar * (diskon / 100)
#     print (f"Anda mendapat Diskon 50%, harga menjadi : {hargaAkhir}")
# else :
#     print (f"harga adalah {hargaDasar}")  

hargaDasar = 50000
diskon = 50
usia = int(input("Masukkan usia: "))

if usia < 12 or usia > 60:
    potongan = hargaDasar * diskon / 100
    hargaAkhir = hargaDasar - potongan
else:
    hargaAkhir = hargaDasar

print(f"Harga yang harus dibayar: {int(hargaAkhir)}")
    



