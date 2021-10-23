#Import Modul Math dan Os
import math as m
import os
import terminaltables

#============================= FUNCTION =================================================+

#fungsi clear screen
def cls():
	command = 'clear'
	if os.name in('nt','dos'):
		command = 'cls'
	else:
		pass
	os.system(command)

#Fungsi Menu Awal Program
def menu():
	cls()
	print("|=================================|")
	print("|   PROGRAM SUBNETTING KELAS C    |")
	print("|=================================|")
	print("| >> AUTHOR ERICK DAE             |")
	print("| >> WibuCode Community           |")
	print("|=================================|")

#fungsi menampilkan tabel prefix
def tabelPrefix():
	kolom = ['NO','BITS/CIDR','JUMLAH IP']
	daftar = [(i+1,listbit[i],listhost[i])for i in range(len(listbit))]

	data_table = [kolom]
	data_table.extend(daftar)
	table = terminaltables.AsciiTable(data_table)
	print("\n| >> TABEL PREFIX ")
	print(table.table)

def angka(pesan):
	while True:
		try:
			ipt = int(input(pesan))
			return ipt
		except ValueError:
			menu()
			tabelPrefix()
			print("\n| [- WARNING -] : Inputan Hanya Menerima Angka")

def looping(pesan):
	ipt = input(pesan)
	while ipt != 'y' and ipt != 't':
		output()
		print("\n|- WARNING -| : Inputan Hanya Menerima Y atau T saja : ")
		ipt = input(pesan)
	return ipt

def output():
	cls()
	print("|=======================================================|")
	print("| >> Diketahui : ")
	print("|-------------------------------------------------------|")
	print("|          >> Prefix/CIDR = /",bit)
	print("|            >> Jumlah Ip = ",jumlahip)
	print("|                >> Hasil = ",ipOktet4,"/",jumlahip," = ",hasil ," = ",final_hasil)
	print("|     >> Ip Awal[NETWORK] = ",final_hasil," * ",jumlahip," = ",ipawal)
	print("| >>  Ip Akhir[BROADCAST] = ",ipawal," + ",jumlahip,"-",1," = ",ipakhir)
	print("|            >> Host Awal = ",ipawal," + ",1," = ",hostawal)
	print("|           >> Host Akhir = ",ipakhir,"+",1," = ",hostakhir)
	print("|          >> Subnet Mask = ",256 ,"-", jumlahip,"=",subnet_mask)
	print("|-------------------------------------------------------|")
	print("|   >> RENTANG IP = ",ipawal," Sampai ",ipakhir)
	print("| >> RENTANG HOST = ",hostawal,"Sampai",hostakhir)
	print("|  >> SUBNET MASK = ",subnet_mask)
	print("|=======================================================|")
	

#=========================== END  FUNCTION =========================================+


#=========================== MAIN ==================================================+
#list tabel prefix
listbit = [24,25,26,27,28,29,30,32]
listhost = [256,128,64,32,16,8,4,1]
ulang = 'y'

while ulang == 'y':
	menu()
	tabelPrefix()

	#inputan cidr/prefix dan ip oktet 4
	iptPrefix = angka("| >> Masukkan CIDR : ")
	#validasi inputan cidr/prefix hanya menerima data dalam listbit
	while iptPrefix not in listbit:
		cls()
		menu()
		tabelPrefix()
		print("\n|- WARNING -| : CIDR Tidak Tersedia Untuk Kelas C")
		iptPrefix = angka("| >> Masukkan CIDR : ")

	#inputan IP Oktet 4
	ipOktet4 = angka("| >> Masukkan Ip Oktet 4 : ")

	#validasi inputan user
	for i in range(len(listbit)):
		if iptPrefix == listbit[i]:
			bit = listbit[i]
			host = listhost[i]
		else:
			pass

	#menghitung
	jumlahip = host
	hasil = ipOktet4/jumlahip
	final_hasil = m.floor(hasil)
	ipawal = final_hasil*jumlahip # IP NETWORK
	ipakhir = ipawal + jumlahip - 1 #IP BROADCAST
	hostawal = ipawal+1
	hostakhir = ipakhir-1
	subnet_mask = 256-jumlahip

	output()
	ulang = looping("| >> Ulangi Program? <Y/T> : ")

print("|---------------------|")
print("| >> PROGRAM BERAKHIR |")
print("|---------------------|")
#=========================== END MAIN ==============================================+