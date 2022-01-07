# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 11:17:35 2021
TRANSAKSI MULTI BARANG DALAM SATU KALI TRANSAKSI
@author: x220
"""

print("")
print("========================================")
print(" DAFTAR MENU ")
print("========================================")
print(" a = COCA COLA   Rp 10.000")
print(" b = AQUA        Rp 5.000")
print(" c = MIZONE      Rp 8.000")
print(" d = ABC KOPI    Rp 3.000")
print(" e = MOCACINO    Rp 15.000")
print("========================================")
print("")

#1. SIAPKAN VARIABEL 
list_nmbrg = [] #untuk simpan seluruh nama barang yang dibeli
list_hrgsat =[] #untuk simpan seluruh harga barang yang dibeli
list_qty=[] #untuk simpan seluruh qty barang yang dibeli
list_totawal =[] #untuk simpan seluruh total awal yang dibeli
cnt=0 #untuk counter banyaknya item yg dibeli
tambah="Y" #untuk default jawaban looping menambah item
tot_bayar=0 #nilai awal total bayar

while tambah=="Y" or tambah=="y":
    kode =['a','b','c','d','e']
    namaBarang = ['COCA COLA','AQUA','MIZONE','ABC KOPI','MOCACINO']
    harga = [10000,5000,8000,3000,15000]

    #2. INPUT PILIHAN
    pilihan = input(">> Masukkan Kode Barang    = ")

    #3. INPUT QTY
    qty     = input(">> Masukkan Jumlah Barang  = ")

    #4. AMBIL NAMA DAN HARGA SATUAN BARANG YG DIPILIH
    ##cek nama barang dan ambil harga satuan
    i = 0
    while i<len(namaBarang):
        #jika value pada list kode[i] == pilihan
        if kode[i] == pilihan:
            #ambil nama barang
            nm_brg = namaBarang[i]

            #ambil harga satuan
            hrgsat = harga[i]
    
        #jika tidak cocok, lanjut ke i berikutnya
        i+=1

    #5. HITUNG BAYAR
    tot_awal = hrgsat * int(qty)


    #6. SIMPAN PADA ITEM PADA LIST BARANG TERBELI
    tot_bayar+=tot_awal
    list_nmbrg.append(nm_brg)
    list_hrgsat.append(hrgsat)
    list_qty.append(int(qty))
    list_totawal.append(tot_awal)
    cnt = cnt + 1

    #7. TAMPILKAN OUTPUT PER BARANG
    print(">>> NAMA BARANG      : " + nm_brg + "\r" )
    print(">>> HARGA BARANG     : " + str(hrgsat) + "\r")
    print(">>> JUMLAH BARANG    : " + qty + "\r")
    print(">>> TOTAL AWAL      : " + str(tot_awal) + "\r")
    print("========================================")

    #8. INPUT TAMBAH ITEM ATAU TIDAK
    tambah = input(">> Tambah Item lagi? ")
    if tambah=="T" or tambah=="t":
        break

#9. JIKA TIDAK ADA TAMBAHAN ITEM, OUTPUT AKHIR:
print("-----------------------------------------")
print(" No.     NAMA      HRG     QTY     TOTAL")
print("-----------------------------------------")
i=0
while i<cnt:
    nourut=i+1
    print(" "+ str(nourut) + "___" + list_nmbrg[i] + "____" +  str(list_hrgsat[i]) + "___" + str(list_qty[i]) + "____" + str(list_totawal[i])) 
    i+=1
print("---------------------------------------")
print(" Total Bayar = " + str(tot_bayar))
print("")
print("")

#SELESAI

"""
#CETAK OUTPUT EXTERNAL
f=open("tesouttransaksi.txt","w+")
#5. TAMPILKAN 
f.write(">>> NAMA BARANG      : " + nm_brg + "\r" )
f.write(">>> HARGA BARANG     : " + str(hrgsat) + "\r")
f.write(">>> JUMLAH BARANG    : " + qty + "\r")
f.write(("-------------------------------\r"))
f.write(">>> TOTAL BAYAR      : " + str(tot_byr) + "\r")

f.write("")
f.write("   - TERIMA KASIH -\r")


1. buatlah agar format uang tersebut memiliki digit ribuan
2. tambahkan fitur Mengulang transaksi
3. Challenge:
    - output ke Notepad
"""

"""
pada materi selanjutnya:
    program akan dibuat agar pembeli dapat membeli 
    beberapa barang sekaligus dalam SATU kali transaksi
    clue: looping pada tambah Item.
"""
