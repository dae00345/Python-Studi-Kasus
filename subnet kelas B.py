from os import system
import math as m
import terminaltables as tm

def cls():
    return system('cls')

def menu():
    cls()
    print("+-----------------------------------------------+")
    print("+              SUBNETTING KELAS B               +")
    print("+-----------------------------------------------+")
    print("+               AUTHOR ERICK DAE                +")
    print("+-----------------------------------------------+")
    print("+ Contoh Ip  = 174.51.230.222/20                +")
    print("+ Prefix     = 20  : (yg ada / bagian akhir)    +")
    print("+ IP Oktet 3 = 230 : (Ip ketiga dari kiri)      +")
    print("+-----------------------------------------------+")


def angka(pesan):
    while True:
        try:
            ipt = int(input(pesan))
        except ValueError:
            menu()
            print("\n|+ WARNING +| : INPUTAN HANYA MENERIMA ANGKA")
        else:
            return ipt
            
def output():
    cls()
    print("|==================================================================|")
    print("| >> PREFIX = ",prefix)
    print("| >> IP OKTET 3  = ",ipAkhir)
    print("|==================================================================|")
    print("| >> Prefix Imagine Kelas C = ",prefix, "+", 8,"=",prefixImagineC)
    print("| >> Jumlah IP Imagine = ",jmlhipc)
    print("| >> Jumlah Ip = ",jmlhipc, "*", 256,"=",jmlhIP)
    print("| >> Hasil = ",ipAkhir,"/",jmlhipc,"=",hasil1)
    print("|==================================================================|")
    print("| >> Rentang IP Awal = ",hasil1,"*",jmlhipc,"=",rentangipAwal)
    print("| >> Rentang IP Akhir = ",rentangipAwal,"+",jmlhipc,"-",1,"=",rentangipAkhir)
    print("| >> Rentang IP Host Awal = ",IPhostawal)
    print("| >> Rentang IP Host Akhir = ",IPhostakhir)
    print("| >> Subnet Mask = 256 - ",jmlhipc)
    print("|==================================================================|")
    print("| >> RENTANG IP = ",rentangipAwal," SAMPAI ",rentangipAkhir)
    print("| >> RENTANG HOST = ",IPhostawal," SAMPAI ",IPhostakhir)
    print("| >> RENTANG IP OKTET 4 SELALU (0 SAMPAI 255)")
    print("| >> RENTANG IP HOST OKTET 4 SELALU (1 SAMPAI 254)")
    print("| >> SUBNET MASK = ",subnetmask)
    print("|==================================================================|")

def output2():
    kolom = ['IP Awal','IP Akhir','Host Awal','Host Akhir','Subnet Mask']
    daftar = [(rentangipAwal,rentangipAkhir,IPhostawal,IPhostakhir,subnetmask)]

    data = [kolom]
    data.extend(daftar)
    tabel = tm.AsciiTable(data)
    print(tabel.table)

def jwb(pesan):
    ipt = input(pesan)
    while ipt != 'y' and ipt != 't':
        output()
        output2()
        print("\n[- WARNING -] : Inputan Hanya Menerima y/t")
        ipt = input(pesan)
    return ipt

#Main
jmlhipc = 0
ulang = 'y'
while ulang == 'y':
    menu()
    prefix = angka("| >> Masukkan Prefix    : ")
    ipAkhir = angka("| >> Masukkan IP Oktet 3 : ")
    prefixImagineC = prefix + 8

    if prefixImagineC == 24:
        jmlhipc = 256
    elif prefixImagineC == 25:
        jmlhipc = 128
    elif prefixImagineC == 26:
        jmlhipc = 64
    elif prefixImagineC == 27:
        jmlhipc = 32
    elif prefixImagineC == 28:
        jmlhipc = 16
    elif prefixImagineC == 29:
        jmlhipc = 8
    elif prefixImagineC == 30:
        jmlhipc = 4
    elif prefixImagineC == 31:
        jmlhipc = 2
    elif prefixImagineC == 32:
        jmlhipc = 1
    else:
        print("Jumlah Ip tidak ditemukan")

    jmlhIP = jmlhipc * 256
    hasil = ipAkhir/jmlhipc
    hasil1 = m.floor(hasil)
    rentangipAwal = hasil1 * jmlhipc
    rentangipAkhir = rentangipAwal + jmlhipc - 1
    IPhostawal = rentangipAwal + 1
    IPhostakhir = rentangipAkhir - 1
    subnetmask = 256-jmlhipc
    output()
    print()
    output2()
    ulang = jwb("\n| >> Ulangi Program? <y/t> : ")