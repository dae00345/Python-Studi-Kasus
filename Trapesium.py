from os import system
from time import sleep

#fungsi clear screen
def cls():
    return system('cls')

#fungsi menampilkan menu utama
def menu():
    cls()
    print("|=======================================|")
    print("|- MENGHITUNG LUAS TRAPESIUM SAMA KAKI -|")
    print("|=======================================|")

#fungsi menampilkan text loading
def loading():
    cls()
    for i in range(5):
        print("Loading...>>>>>>")
        sleep(0.2)

#fungsi menampilkan output luas   
def output():
    cls()
    print("|===================================|")
    print("| -            OUTPUT             - |")
    print("|-----------------------------------|")
    print("| >> Diketahui :                    |")
    print("|-----------------------------------|")
    print("| >> Panjang Sisi Atas  = ",iptA)
    print("| >> Panjang Sisi Bawah = ",iptB)
    print("| >> Tinggi             = ",iptT)
    print("|-----------------------------------|")
    print("| >> Penyelesaian :                 |")
    print("|-----------------------------------|")
    print("| >> =","1/2 *(",iptA, "+",iptB,")*",iptT)
    print("| >> = 1/2 *",iptA+iptB,"*",iptT)
    print("| >> = ",1/2 * (iptA+iptB),"*",iptT)
    print("| >> = ",1/2 * (iptA + iptB) * iptT)
    print("|-----------------------------------|")
    print("| >> Luas : ",luas)
    print("|===================================|")

#fungsi validasi inputan hanya menerima angka
def angka(pesan):
    while True:
        try:
            ipt = float(input(pesan))
        except ValueError:
            menu()
            print("\n|- WARNING -| : INPUTAN HANYA MENERIMA ANGKA")
        else:
            return ipt

#fungsi validasi inputan hanya menerima y/t saja
def jwb(pesan):
    ipt = input(pesan).lower()
    while ipt != "y" and ipt !="t":
        print("|- WARNING -| : Inputan Hanya Menerima y/t saja")
        menu()
        output()
        ipt = input(pesan).lower()
    return ipt

#Main
ulang = 'y'
while ulang == 'y':
    menu()
    iptA = angka("| >> Panjang sisi atas  : ")
    iptB = angka("| >> Panjang sisi bawah : ")
    iptT = angka("| >> Tinggi             : ")
    luas = 1/2 * (iptA + iptB) * iptT
    loading()
    output()
    ulang = jwb("| >> Hitung lagi? <y/t> : ")
