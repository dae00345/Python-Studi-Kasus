"""
Nama  :
Nim   :
Kelas :
Prodi :
Fakultas :

Ket:
	Pastikan sudah menginstal modul terminaltables untuk menjalankan source code ini
	Bisa melalui command prompt dengan perintah pip install terminaltables
"""

import os
import terminaltables

#fungsi clearscreen 
def cls():
	command = 'clear'
	if os.name in ('nt','dos'):
		command = 'cls'
	os.system(command)

#validasi inputan hanya menerima angka
def angka(pesan):
	while True:
		try:
			ipt = int(input(pesan))
			return ipt
		except ValueError:
			outputKasir()
			print("|- WARNING -| : Inputan Hanya Menerima Angka")

#validasi inputan hanya menerima angka1
def angka1(pesan):
	while True:
		try:
			ipt = int(input(pesan))
			return ipt
		except ValueError:
			cls()
			outputDataBarang()
			print("|- WARNING -| : Inputan Hanya Menerima Angka")

#fungsi menampilkan data kode kasir dan nama kasir
def outputKasir():
	cls()
	kolom = ['KODE KASIR','NAMA BARANG']
	daftar = [(listKodeKasir[i],listNamaKasir[i]) for i in range(len(listKodeKasir))]

	data_table = [kolom]
	data_table.extend(daftar)

	table = terminaltables.AsciiTable(data_table)

	print("|--------------------------|")
	print("|           KASIR          |")
	print(table.table)

#fungsi menampilkan data barang
def outputDataBarang():
	kolom = ['KODE','NAMA BARANG','HARGA PERKG']
	daftar = [(listKodeBarang[i],listNamaBarang[i],format(listharga[i],",.2f"))for i in range(len(listKodeBarang))]

	data_table = [kolom]
	data_table.extend(daftar)
	table = terminaltables.AsciiTable(data_table)

	print("|---------------------------------------|")
	print("|              DAFTAR BARANG            |")
	print(table.table)

def outputakhirKasir():
	cls()
	print("|----------------------------------------------------------------------------|")
	print("|                         TOKO BUAH SEGAR SELALU                             |")
	print("|----------------------------------------------------------------------------|")
	print("| >> No Transaksi : ",iptNoTransaksi,"                         >> Nama Kasir : ",namakasir)

def outputAkhir():
	kolom = ['NO','KODE BUAH','NAMA BUAH','HARGA BUAH','JUMLAH BELI','TOTAL HARGA','DISKON','HARGA BAYAR']
	daftar = [(i+1,listKodeBuah[i],listNamaBuah[i],format(listHargaBuah[i],",.2f"),listJumlahBeli[i],format(listTotalHarga[i],",.2f"),format(listDiskon[i],",.2f"),format(listHargaBayar[i],",.2f"))for i in range(len(listKodeBuah))]

	data_table = [kolom]
	data_table.extend(daftar)
	table = terminaltables.AsciiTable(data_table)

	print(table.table)


#fungsi menampilkan tampilan akhir program
#MAIN
counter = 0

#List kode kasir dan nama kasir
listKodeKasir = ['SLM','YDI','SND']
listNamaKasir = ['Salim','Yudi','Sandra']

#list kodebarang nama barang dan harga barang
listKodeBarang = ['PS','AG','KW','NG']
listNamaBarang = ['Pisang Sunpride','Anggur','Kiwi Green Hijau','Naga Premium']
listharga = [20_000,45_000,50_000,25_000]

#list sebagai temp storage untuk menampung semua belanjaan
listKodeBuah = []
listNamaBuah = []
listHargaBuah = []
listJumlahBeli = []
listTotalHarga = []
listDiskon = []
listHargaBayar = []

#Menampikan data kasir 
outputKasir()

#inputan Nomor Transaksi dan Kode Kasir
iptNoTransaksi = angka("| >> Masukkan Nomor Transaksi : ")
iptKodeKasir = input("| >> Masukkan Kode Kasir : ").upper()


#validasi inputan kode kasir hanya menerima kode dalam list saja
while iptKodeKasir not in listKodeKasir:
	outputKasir()
	print("|- WARNING -| : KODE KASIR TIDAK TERSEDIA")
	iptKodeKasir = input("| >> Masukkan Kode Kasir : ").upper()

#validasi pilihan kasir 
for i in range(len(listKodeKasir)):
	if iptKodeKasir == listKodeKasir[i]:
		kodekasir = listKodeKasir[i]
		namakasir = listNamaKasir[i]
	else:
		pass

#Inputan Jumlah Data
iptJumlahData = angka("| >> Masukkan Jumlah Data : ")
while counter < iptJumlahData:
	counter+=1
	cls()
	outputDataBarang()
	print("|--------------------------------------|")
	print("| >> DATA KE ",counter)
	print("|--------------------------------------|")

	#inputan kode buah sekaligus validasi inputan hanya menerima elemen yang ada di dalam list kode barang
	iptkodebuah = input("| >> Masukkan Kode Buah : ").upper()
	while iptkodebuah not in listKodeBarang:
		cls()
		outputDataBarang()
		print("|- WARNING -| : Kode Buah Tidak Tersedia")
		iptkodebuah = input("| >> Masukkan Kode Buah : ").upper()

	iptJumlahBeli = angka1("| >> Masukkan Jumlah Beli : ")

	#validasi inputan user 
	for i in range(len(listKodeBarang)):
		if iptkodebuah == listKodeBarang[i]:
			brg = listKodeBarang[i]
			namabrg = listNamaBarang[i]
			hrg = listharga[i]
		else:
			pass

	total_harga = iptJumlahBeli * hrg
	diskon = 0

	#diskon
	if iptJumlahBeli > 5 :
		diskon = 0.05 * total_harga
	elif iptJumlahBeli > 10 :
		diskon = 0.08 * total_harga
	else:
		diskon = 0

	harga_bayar = total_harga - diskon

	#Memasukan Semua belanjaan kedalam temp storage
	listKodeBuah.append(iptkodebuah)
	listNamaBuah.append(namabrg)
	listHargaBuah.append(hrg)
	listJumlahBeli.append(iptJumlahBeli)
	listTotalHarga.append(total_harga)
	listDiskon.append(diskon)
	listHargaBayar.append(harga_bayar)

#output tampilan akhir
outputakhirKasir()
outputAkhir()

jmlhby = sum(listHargaBayar)
ppn = 0.1 * jmlhby
totby = jmlhby + ppn
print(f"|--------------------------------------------------|")
print(f"| >> Jumlah Bayar = Rp.{jmlhby:,}")
print(f"| >> PPN          = Rp.{ppn:,}")
print(f"| >> Total Bayar  = Rp.{totby:,}")
print(f"|--------------------------------------------------|")



iptexit = input("\n\n >> Tekan enter untuk keluar")




