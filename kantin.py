pembeli = input("Masukkan nama Pembeli: ")
print("===============================================================")

print ("Nama Pembeli :", pembeli) 

print("===============================================================")

print("KANTIN HARBER")

print("Menu Makanan")
print(" 1. Ayam Geprek :Rp 13000")
print(" 2. Soto Betawi :Rp 10000")
print(" 3. Nasi Campur :Rp 10000")

list_menu=str(input("Masukkan angka sesuai dengan menu yang tersedia = "))
jumlahPesanan=int(input("Jumlah dibeli = "))

if list_menu == "1":
        nama_menu= "Ayam Geprek"
        harga=(13000*jumlahPesanan)
elif list_menu == "2":
        nama_menu= "Soto Betawi"
        harga = (10000*jumlahPesanan)
elif list_menu == "3":
        nama_menu= "Nasi Campur"
        harga=int(10000*jumlahPesanan)
else:
    print("Menu Tidak Tersedia")

print("===============================================================")

print("Menu :",nama_menu)
print("Jumlah pesanan :", jumlahPesanan)
print("Total pembayaran :", harga)

print("===============================================================")

metode_pembayaran = input("Pilih metode pembayaran (tunai/non-tunai) :")
if metode_pembayaran == "tunai":
    print("Silakan bayar sesuai total pembelian.")
elif metode_pembayaran == "non-tunai":
    nomor_kartu = input("Masukkan nomor kartu: ")
    print("Pembayaran sukses.")
else:
    print("Metode pembayaran tidak valid.")

