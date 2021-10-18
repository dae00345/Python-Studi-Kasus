from os import system
import math as m

def cls():
    return system('cls')

def menu():
    cls()
    print("|-------------------------------|")
    print("+      SUBNETTING KELAS C       +")
    print("|------------ NOTE -------------|")
    print("| JUMLAH IP DILIHAT DARI PREFIX |")
    print("|-------------------------------|")

def angka(pesan):
    while True:
        try:
            ipt = int(input(pesan))
        except ValueError:
            menu()
            print("\n|+ WARNING +| : INPUTAN HANYA MENERIMA ANGKA")
        else:
            return ipt
def kelasc():
    print("|+------------------------------+|")
    print("|+ >> Penyelesaian :            +|")
    print("|+------------------------------+|")
    print("| >> Jumlah Ip : ",jmlhIp)
    print("| >> IP Akhir  : ",lastIP)
    print("|+------------------------------+|")
    print("| >> =  ",lastIP,"/",jmlhIp," = ",hasil1)
    print("|+------------------------------+|")
    print("| >> Rentang Awal Ip  : \n    | >",hasil1,"*",jmlhIp," = ",rentangip)
    print("| >> Rentang Akhir Ip : \n   | >",rentangip,"+",jmlhIp,"-", 1 ,"=",rentangipakhirip)
    print("|+----------- NOTE -------------+|")
    print("| >> Rentang Awal = Ip Network")
    print("| >> Rentang Akhir = Ip Broadcast ")
    print("|+------------------------------+|")
    print("| >> Rentang Awal IP Host  = : ",rentangawaliphost)
    print("| >> Rentang Akhir IP Host = : ",rentangakhiriphost)
    print("|+------------------------------+|")
    print("| >> Subnet Mask = ",256,"-",jmlhIp,"=",subnetMask)
    print("| >> RENTANG IP  = ",rentangip," Sampai ",rentangipakhirip)
    print("| >> Rentang Ip Host = ",rentangawaliphost," Sampai ",rentangakhiriphost)
    print("|+------------------------------+|")

#Main
menu()
jmlhIp = angka("|+ >> Masukkan Jumlah IP : ")
lastIP = angka("|+ >> Masukkan Ip Akhir  : ")
hasil = lastIP/jmlhIp
hasil1 = m.floor(hasil)
rentangip = hasil1 * jmlhIp
rentangipakhirip = rentangip + jmlhIp - 1
rentangawaliphost = rentangip + 1
rentangakhiriphost = rentangipakhirip - 1
subnetMask = 256-jmlhIp
#penyelesaian
kelasc()

iptexit = input("\nPress anykey to exit")

