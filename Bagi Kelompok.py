import random

nama = list(input("Masukkan nama (pisahkan dengan spasi) = ").split())
jumlah_kelompok = int(input("Jumlah kelompok = "))
kelompok = [""]*jumlah_kelompok

i = 0
while len(nama)!=0:
    jumlah_orang = len(nama)
    terpilih = random.randint(0, jumlah_orang-1)
    kelompok[i] = kelompok[i] + " " + nama[terpilih]
    del nama[terpilih]
    i += 1
    if i == jumlah_kelompok:
        i = 0
    
for i in range(jumlah_kelompok):
    print("Kelompok", str(i+1) + ":" + kelompok[i])
