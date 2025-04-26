import pickle
from datetime import datetime
tanggal = datetime.now()


class Transaksi:
    def __init__(self, nama, jumlah, kategori,tanggal):
        self.nama = nama
        self.jumlah = jumlah
        self.kategori = kategori
        self.tanggal = tanggal
        

def cetak(transaksi):
    print(f" {transaksi.tanggal.strftime('%d-%m %y:')}, {transaksi.nama}, Rp{transaksi.jumlah}, kategori: {transaksi.kategori}")


saldo = 0
daftar_pemasukan = []
daftar_penegluaran = []

try:
    with open("saldo.txt" , "r") as file:
        saldo = int(file.read())

    with open("daftar_pemasukan.txt" , "rb") as file:
        daftar_pemasukan = pickle.load(file)

    with open("daftar_pengeluaran.txt" , "rb") as file:
        daftar_penegluaran = pickle.load(file)

except FileNotFoundError:
    with open("saldo.txt" ,"w") as file:
            file.write(str(0))
    print("tidak ada catatan")



while True:
    print("1. pemasukan ")
    print("2. pengeluaran ")
    print("3. riwayat tranksaksi ")
    print("4. sisa saldo ")
    print("5. exit")
   
    pilihan_anda = int(input("Masukan pilihan anda : "))

    if pilihan_anda == 1:
        nama = input("nama pemasukan :")
        jumlah = int(input("masukan jumlah :"))
        saldo = saldo + jumlah
        kategori = str(input("masukan kategori pemasukan :"))
        transaksi_baru = Transaksi(nama= nama, jumlah= jumlah, kategori= kategori, tanggal= tanggal )

        with open("saldo.txt" ,"w") as file:
            file.write(str(saldo))
        
        daftar_pemasukan.append(transaksi_baru)
        with open("daftar_pemasukan.txt" , "wb") as file:
            pickle.dump(daftar_pemasukan,file)

        cetak(transaksi_baru)
        print(f"transaksi berhasil di simpan")



    elif pilihan_anda == 2:
        nama = input("nama pengeluaran :")
        jumlah = int(input("masukan jumlah :"))
        kategori = str(input("masukan kategori pengeluaran :"))
        transaksi_baru = Transaksi(nama= nama, jumlah= jumlah, kategori= kategori, tanggal = tanggal)
        saldo = saldo - jumlah

        with open("saldo.txt" ,"w") as file:
            file.write(str(saldo))

        daftar_penegluaran.append(transaksi_baru)
        with open("daftar_pengeluaran.txt" , "wb") as file:
            pickle.dump(daftar_penegluaran,file)

        cetak(transaksi_baru)
        print(f"transaksi berhasil di simpan")


    elif pilihan_anda == 3:
        for catatan in daftar_pemasukan:
            print("histori pemasukan :")
            cetak(catatan)

            

        for catatan in daftar_penegluaran:
            print("histori pengeluaran :")
            cetak(catatan)

    
    elif pilihan_anda == 4:
        print("sisa saldo anda:", saldo)
        
         

    elif pilihan_anda == 5:
        break



