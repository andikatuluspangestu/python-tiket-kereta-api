# Import Module atau Library OS
# Dengan import OS kita bisa menghapus secara otomatis text sebelumnya
# Dengan import platform kita bisa mendeteksi secara otomatis sistem operasi komputer kita
# Dengan import random kita bisa meregenerate secara acak kode pesan tiket otomatis
import os
import platform
import random

########################################################################
#############   SISTEM FUNCTION TIKET : List menu dll.  ################
########################################################################

# Function Membersihkan Terminal
def clearTerminal():
	# Untuk sistem Windows
	if( platform.system() == "Windows" or platform.system() == "Win" ):
		clear = lambda: os.system('cls')
		clear()
	if( platform.system() == "Linux" ):
		clear = lambda: os.system('clear')
		clear()

# Function list menu
def list_menu():
	print("=" * 36)
	print("Aplikasi Pesan Tiket Stasiun Tegal")
	print("-" * 36)
	print("1. Pilih Kota Tujuan")
	print("2. Keluar Aplikasi")
	print("-" * 36)

# Function List Kota
def list_kota():
	print("=" * 36)
	print("Daftar Tujuan Kota Tersedia")
	print("-" * 36)
	print("1. Semarang")
	print("2. Surabaya")
	print("3. Yogyakarta")

# Function Hitung Total tiket dan Strukt
def pemesanan():

	print("-" * 36)
	print("Mengisi Data Pemesanan")
	print("-" * 36)

	# Masukan Jumlah Tiket
	print("Masukan Jumlah Tiket yang akan dipesan")
	beli_tiket = int(input("> Masukan Jumlah Tiket : "))

	# List atau Array menampung jumlah pemesan Tiket
	list_nama_penumpang = list()

	# # Masukan Jumlah orang yang memesan tiket
	# jumlah_pemesan = input("Berapa orang yang ingin memesan tiket ? : ")
	
	# Masukan nama orang pemesan tiket
	# Lakukan looping untuk menampilkan pemesan tiket
	print("Masukan Nama Penumpang Kereta Api")
	for urutanPemesan in range (beli_tiket):
		urutanPemesan += 1
		namaPemesan = input("> Masukan Nama Pemesan ke {} : ".format(urutanPemesan))
		list_nama_penumpang.append(str(namaPemesan)) 

	# Bersihkan Terminal
	clearTerminal()

	# Hitung total harga tiket
	total_harga_tiket = beli_tiket * harga_tiket
	
	# Cetak Struk
	print("-" * 46)
	print("   PT. Kereta API Indonesia - Stasiun Tegal   ")
	print("-" * 46)
	print("Kode Pemesanan Tiket : ", random.randint(1000,9999))
	print("Nama Kereta Api      : ", namaKereta)
	print("Kota Tujuan          : ", pilihan_kota)
	print("Nama Pemesan         : ".format(len(list_nama_penumpang)))
	# Lakukan looping untuk menampilkan total harga tiket
	for harga_tiket_dibeli in list_nama_penumpang:
		print (("- {}").format(harga_tiket_dibeli))
	print("-" * 46)
	print("Total Harga Tiket adalah","Rp.",(total_harga_tiket))
	print("-" * 46)
	print("")

# Perulangan Untuk mengkonfirmasi pemesanan tiket kembali
def konfirmasi_pemesanan_ulang():
	while(input("Apakah anda ingin memesan tiket kembali? [Y/T] ... ") == "Y"):
    # Jika pengguna menginput "Y" maka akan menampilkan list kota lagi.
    		list_kota()
	# Jika tidak, maka tampilkan terima kasih dan keluar aplikasi
	print("Baik, Terima Kasih telah menggunakan aplikasi kami :) ")


########################################################################
############# SISTEM PEMESANAN TIKET : Percabangan dll. ################
########################################################################

# Menampilkan list menu aplikasi
list_menu()

# Keputusan pemilihan menu aplikasi
pilihan_menu = int(input("Masukan Pilihan Anda : "))
print("-" * 36)

# Percabangan Pemilihan menu aplikasi
if(pilihan_menu == 1):
	# Menampilkan List Kota
	clearTerminal()
	list_kota()

	# Keputusan pemilihan kota tujuan
	print("-" * 36)
	pilihan_kota = input("Masukan Nama Kota Tujuan Anda : ")
	print("-" * 36)

	# Percabangan bersarang untuk list kereta api
	# Semarang
	clearTerminal()
	print("=" * 55)
	print("Daftar Kereta Api yang Tersedia untuk Jurusan ", pilihan_kota)
	print("-" * 55)
	if(pilihan_kota == "Semarang" or pilihan_kota == "semarang"):
		# List Kereta Api Semarang
		print("1. Kaligung Eksekutif")
		print("2. Kamandaka")
		# Keputusan pemilihan kereta api
		pilihan_kereta = int(input("Masukan Pilihan Kereta Anda : "))
		if(pilihan_kereta == 1):
			harga_tiket = 60000
			namaKereta = "Kaligung Eksekutif"
			clearTerminal()
			print("Kamu memilih Kereta Api KA Kaligung Eksekutif")
			pemesanan()
			konfirmasi_pemesanan_ulang()
		elif(pilihan_kereta == 2):
			harga_tiket = 50000
			namaKereta = "Kamandaka"
			clearTerminal()
			print("Kamu memilih Kereta Api KA Kamandaka")
			pemesanan()
			konfirmasi_pemesanan_ulang()

	# Surabaya
	elif(pilihan_kota == "Surabaya" or pilihan_kota == "surabaya"):
		# List Kereta Api Surabaya
		print("1. KA Jayabaya")
		print("2. KA Kertajaya")
		# Keputusan pemilihan kereta api
		pilihan_kereta = int(input("Masukan Pilihan Kereta Anda : "))
		if(pilihan_kereta == 1):
			harga_tiket = 315000
			namaKereta = "KA Jayabaya"
			clearTerminal()
			print("Kamu memilih Kereta Api KA Jayabaya")
			pemesanan()
			konfirmasi_pemesanan_ulang()
		elif(pilihan_kereta == 2):
			harga_tiket = 150000
			namaKereta = "KA Kertajaya"
			clearTerminal()
			print("Kamu memilih Kereta Api KA Kertajaya")
			pemesanan()
			konfirmasi_pemesanan_ulang()
		
	# Yogyakarta
	elif(pilihan_kota == "Yogyakarta" or pilihan_kota == "yogyakarta"):
		# List Kereta Api Yogyakarta
		print("1. KA Fajar Utama")
		print("2. KA Senja Utama")
		# Keputusan pemilihan kereta api
		pilihan_kereta = int(input("Masukan Pilihan Kereta Anda : "))
		if(pilihan_kereta == 1):
			harga_tiket = 300000
			namaKereta = "KA Fajar Utama"
			clearTerminal()
			print("Kamu memilih Kereta Api KA Fajar Utama")
			pemesanan()
			konfirmasi_pemesanan_ulang()
		elif(pilihan_kereta == 2):
			harga_tiket = 215000
			namaKereta = "KA Senja Utama"
			clearTerminal()
			print("Kamu memilih Kereta Api KA Senja Utama")
			pemesanan()
			konfirmasi_pemesanan_ulang()

	# List kota tidak tersedia
	else:
		clearTerminal()
		print("Pilihan Kota yang anda masukan tidak tersedia")

# Pilihan menu aplikasi ke dua ( Keluar Aplikasi )
elif(pilihan_menu == 2):
	clearTerminal()
	print("Terima kasih,telah menggunakan aplikasi kami")
	exit()

# Source Under MIT License by Andika Tulus Pangestu dan Nafatul Adistianingrum