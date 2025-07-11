from data_manager import load_data, save_data
from transaksi import catat_transaksi, tampilkan_laporan, update_transaksi, hapus_transaksi
from kategori import tampilkan_per_kategori

def main():
    data = load_data()
    
    while True:
        print(" Aplikasi Manajemen KeuanganKu: ")
        print("1. Catat Transaksi")
        print("2. Tampilkan Laporan")
        print("3. Tampilkan Pengeluaran per Kategori")
        print("4. Update Transaksi")
        print("5. Hapus Transaksi")
        print("0. Keluar")
        pilihan = input("Pilih menu (1/2/3/4/5/0): ")

        if pilihan == '1':
            catat_transaksi(data)
        elif pilihan == '2':
            tampilkan_laporan(data)
        elif pilihan == '3':
            tampilkan_per_kategori(data)
        elif pilihan == '4':
            update_transaksi(data)
        elif pilihan == '5':
            hapus_transaksi(data)
        elif pilihan == '0':
            save_data(data)
            print("Data disimpan. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.\n")

if __name__ == '__main__':
    main()