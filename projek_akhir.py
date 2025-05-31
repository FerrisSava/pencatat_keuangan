from tkinter import*
from tkinter import messagebox
import pickle
from datetime import datetime
tanggal = datetime.now()
window = Tk()

saldo = 0
daftar_pemasukan = []
daftar_pengeluaran = []

class Transaksi:
    def __init__(self, nama, jumlah, kategori,tanggal):
        self.nama = nama
        self.jumlah = jumlah
        self.kategori = kategori
        self.tanggal = tanggal


        

def cetak(transaksi):
    print(f" {transaksi.tanggal.strftime('%d-%m %y:')}, {transaksi.nama}, Rp{transaksi.jumlah}, kategori: {transaksi.kategori}")

def open_pemasukan():
    window_pemasukan = Toplevel(window)
    window_pemasukan.title("Pemasukan")
    window_pemasukan.geometry("250x280")
    window_pemasukan.transient(window)
    window_pemasukan.grab_set()
    window_pemasukan.attributes("-topmost",True)

   

    Label(window_pemasukan, text="Nama").pack(pady=(30,0))
    entry_nama = Entry(window_pemasukan)
    entry_nama.pack()

    Label(window_pemasukan, text="Kategori").pack(pady=(30,0))
    entry_kategori = Entry(window_pemasukan)
    entry_kategori.pack()

    Label(window_pemasukan, text="Jumlah").pack(pady=(30,0))
    entry_jumlah = Entry(window_pemasukan)
    entry_jumlah.pack()
    
    Button(window_pemasukan, text="Simpan", command=lambda:simpan_pemasukan(entry_nama.get(),(entry_jumlah.get()), (entry_kategori.get()),window_pemasukan), width=20).pack(pady=15)

    window_pemasukan.resizable(False, False)
    print("membuka pemasukan")

def open_pengeluaran():
    window_pengeluaran = Toplevel(window)
    window_pengeluaran.title("Pengeluaran")
    window_pengeluaran.geometry("250x280")
    window_pengeluaran.transient(window)
    window_pengeluaran.grab_set()
    window_pengeluaran.attributes("-topmost",True)


    Label(window_pengeluaran, text="nama").pack(pady=(30,0))
    entry_nama= Entry(window_pengeluaran)
    entry_nama.pack()

    Label(window_pengeluaran, text="Kategori").pack(pady=(30,0))
    entry_kategori= Entry(window_pengeluaran)
    entry_kategori.pack()

    Label(window_pengeluaran, text="Jumlah").pack(pady=(30,0))
    entry_Jumlah= Entry(window_pengeluaran)
    entry_Jumlah.pack()

    Button(window_pengeluaran, text="Simpan", command=lambda:simpan_pengeluaran(entry_nama.get(),(entry_Jumlah.get()), (entry_kategori.get()),window_pengeluaran), width=20).pack(pady=15)

    window_pengeluaran.resizable(False, False)
    print("membuka pengeluaran")

def open_riwayat_transaksi():
    window_transaksi = Toplevel(window)
    window_transaksi.title("Transaksi")
    window_transaksi.geometry()

    Label(window_transaksi, text = "Daftar pemasukan",font= ("Arial",10,"bold"),anchor="w" ).pack(pady=(30,0),fill="x" )
         

    for catatan in daftar_pemasukan:
         
        Label(window_transaksi, text =f"tanggal: {catatan.tanggal.strftime('%d-%m %y %H:%M')}, nama: {catatan.nama}, jumlah: {catatan.jumlah}, kategori: {catatan.kategori}",anchor="w").pack(pady=(5,0), fill="x")
         
    Label(window_transaksi, text = "Daftar pengeluaran",font= ("Arial",10,"bold"), anchor="w" ).pack(pady=(30,0), fill="x")
         

    for catatan in daftar_pengeluaran:
         
        Label(window_transaksi, text =f"tanggal: {catatan.tanggal.strftime('%d-%m %y %H:%M')}, nama: {catatan.nama}, jumlah: {catatan.jumlah}, kategori: {catatan.kategori}", anchor="w").pack(pady=(5,0), fill="x")
         
    
    print("membuka riwayat transaksi")

def open_sisa_saldo():

    with open("saldo.txt" , "r") as file:
        saldo = int(file.read())


    window_sisa_saldo = Toplevel(window)
    window_sisa_saldo.title("Transaksi")
    window_sisa_saldo.geometry()

    Label(window_sisa_saldo, text = saldo ,font= ("Arial",10,"bold"), ).pack(pady=(30) )
         
    
    print("membuka sisa saldo")

def simpan_pemasukan(nama, jumlah, kategori, window_pemasukan):
    if nama == "":
        messagebox.showerror("terjadi kesalahan", "nama tidak boleh kosong!") 
        return
    if jumlah == "" or int(jumlah)<0:
        messagebox.showerror("terjadi kesalahan","jumlah tidak boleh kosong!")
        return
    if kategori == "":
        messagebox.showerror("terjadi kesalahan","kategori tidak boleh kosong!")
        return


    with open("saldo.txt" , "r") as file:
        saldo = int(file.read())

   
    transaksi_baru = Transaksi(nama= nama, jumlah= int(jumlah), kategori= kategori, tanggal= tanggal )
    temp_saldo = saldo + transaksi_baru.jumlah
    with open("saldo.txt" ,'w') as file:
        file.write(str(temp_saldo))
    
    daftar_pemasukan.append(transaksi_baru)
    with open("daftar_pemasukan.txt" , "wb") as file:
        pickle.dump(daftar_pemasukan,file)
    
    response = messagebox.showinfo("pemasukan","berhasil meyimpan!")
    if response == "ok":
        window_pemasukan.destroy()
    
    

def simpan_pengeluaran(nama, jumlah, kategori, window_pengeluaran):
    if nama == "":
        messagebox.showerror("terjadi kesalahan", "nama tidak boleh kosong!") 
        return
    if jumlah == "" or int(jumlah)<0:
        messagebox.showerror("terjadi kesalahan","jumlah tidak boleh kosong!")
        return
    if kategori == "":
        messagebox.showerror("terjadi kesalahan","kategori tidak boleh kosong!")
        return
    
    with open("saldo.txt" , "r") as file:
        saldo = int(file.read())

   
    transaksi_baru = Transaksi(nama= nama, jumlah= int(jumlah), kategori= kategori, tanggal= tanggal )

    temp_saldo_pengeluaran = saldo - transaksi_baru.jumlah
    with open("saldo.txt" ,"w") as file:
        file.write(str(temp_saldo_pengeluaran))
    
    daftar_pengeluaran.append(transaksi_baru)
    with open("daftar_pengeluaran.txt" , "wb") as file:
        pickle.dump(daftar_pengeluaran,file)

    response = messagebox.showinfo("pengeluaran","berhasil meyimpan!")
    if response == "ok":
        window_pengeluaran.destroy()
    


try:
    with open("saldo.txt" , "r") as file:
        saldo = int(file.read())

    with open("daftar_pemasukan.txt" , "rb") as file:
        daftar_pemasukan = pickle.load(file)

    with open("daftar_pengeluaran.txt" , "rb") as file:
        daftar_pengeluaran = pickle.load(file)

except FileNotFoundError:
    with open("saldo.txt" ,"w") as file:
            file.write(str(0))
    print("tidak ada catatan")

window.geometry("250x260")
window.title("pencatat keuangan")

Button(window, text= "Pemasukan", command=open_pemasukan, width= 20, font= ("Arial",10,"bold")).pack(pady=(25,0))
Button(window, text= "Pengeluaran", command=open_pengeluaran, width= 20, font= ("Arial",10,"bold")).pack(pady=(25,0))
Button(window, text= "Riwayat transaksi", command=open_riwayat_transaksi, width= 20, font= ("Arial",10,"bold")).pack(pady=(25,0))
Button(window, text= "Sisa saldo", command=open_sisa_saldo, width= 20, font= ("Arial",10,"bold")).pack(pady=25)

window.resizable(False,False)

window.mainloop()

# print("login")
# print("1. pemasukan ")
# print("2. pengeluaran ")
# print("3. riwayat tranksaksi ")
# print("4. sisa saldo ")
# print("5. exit")

# pilihan_anda = int(input("Masukan pilihan anda : "))

# if pilihan_anda == 1:
#     nama = input("nama pemasukan :")
#     jumlah = int(input("masukan jumlah :"))
#     saldo = saldo + jumlah
#     kategori = str(input("masukan kategori pemasukan :"))
#     transaksi_baru = Transaksi(nama= nama, jumlah= jumlah, kategori= kategori, tanggal= tanggal )

#     with open("saldo.txt" ,"w") as file:
#         file.write(str(saldo))
    
#     daftar_pemasukan.append(transaksi_baru)
#     with open("daftar_pemasukan.txt" , "wb") as file:
#         pickle.dump(daftar_pemasukan,file)

#     cetak(transaksi_baru)
#     print(f"transaksi berhasil di simpan")



# elif pilihan_anda == 2:
#     nama = input("nama pengeluaran :")
#     jumlah = int(input("masukan jumlah :"))
#     kategori = str(input("masukan kategori pengeluaran :"))
#     transaksi_baru = Transaksi(nama= nama, jumlah= jumlah, kategori= kategori, tanggal = tanggal)
#     saldo = saldo - jumlah

#     with open("saldo.txt" ,"w") as file:
#         file.write(str(saldo))

#     daftar_pengeluaran.append(transaksi_baru)
#     with open("daftar_pengeluaran.txt" , "wb") as file:
#         pickle.dump(daftar_pengeluaran,file)

#     cetak(transaksi_baru)
#     print(f"transaksi berhasil di simpan")


# elif pilihan_anda == 3:
#     for catatan in daftar_pemasukan:
#         print("histori pemasukan :")
#         cetak(catatan)

        

#     for catatan in daftar_pengeluaran:
#         print("histori pengeluaran :")
#         cetak(catatan)


# elif pilihan_anda == 4:
#     print("sisa saldo anda:", saldo)
    
        




