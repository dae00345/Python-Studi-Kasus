
import terminaltables as tb
from os import system

def cls():
    return system('cls')

def angka(pesan):
    while True:
        try:
            ipt = int(input(pesan))
            return ipt
        except ValueError:
            menu()
            print("\n [WARNING] : INPUTAN HANYA MENERIMA ANGKA")

def menu():
    kolom = ["KODE","KOTA","JARAK KM","HARGA"]
    daftar = [(listpil[i],listkota[i],listjarak[i],format(listharga[i],",.2f"))for i in range(len(listpil))] 

    data_table = [kolom]
    data_table.extend(daftar)
    table = tb.AsciiTable(data_table)

    cls()
    print("+ >> PILIHAN")
    print(table.table)

def output1():
    kolom = ["Tujuan","Jarak Km","Ongkir PerKm","Total Biaya"]
    daftar = [(kota,jarak,format(harga,",.2f"),format(totby,",.2f"))]

    data = [kolom]
    data.extend(daftar)
    table = tb.AsciiTable(data)
    cls()
    print("+ HASIL PERHITUNGAN")
    print(table.table)

def looping(pesan):
    ipt = input(pesan).lower()
    while ipt != 'y' and ipt != 't':
        output1()
        print("\n [WARNING] : INPUTAN HANYA MENERIMA Y/T")
        ipt = input(pesan).lower()
    return ipt


#Main
listpil = [1,2]
listkota = ['Surabaya','Bandung']
listjarak = [169,452]
listharga = [2500,4000]
ulang = 'y'

while ulang == 'y':
    menu()
    iptpil = angka("\n\b| >> Pilihan : ")
    while iptpil not in listpil:
        menu()
        print("\n[WARNING] : INPUTAN TIDAK TERSEDIA")
        iptpil = angka("\n\b| >> Pilihan : ")

    for i in range(len(listpil)):
        if iptpil == listpil[i]:
            pil = listpil[i]
            kota = listkota[i]
            jarak = listjarak[i]
            harga = listharga[i]
            totby = harga*jarak
        else:
            pass
        
    output1()
    ulang = looping("\n| >> Hitung lagi? : ")




