from datetime import datetime

def catat_transaksi(data):
    tanggal = input("Masukkan tanggal (YYYY-MM-DD): ")
    jenis = input("Jenis (pemasukan/pengeluaran): ")
    jumlah = input("Jumlah: Rp ")
    kategori = input("Kategori: ")

    transaksi = {
        'tanggal': tanggal,
        'jenis': jenis,
        'jumlah': jumlah,
        'kategori': kategori
    }
    data.append(transaksi)
    print("Transaksi berhasil dicatat.\n")

def tampilkan_laporan(data):
    total_masuk = sum(int(d['jumlah']) for d in data if d['jenis'] == 'pemasukan')
    total_keluar = sum(int(d['jumlah']) for d in data if d['jenis'] == 'pengeluaran')

    print(" Laporan Keuangan ")
    print(f"Total Pemasukan: Rp{total_masuk}")
    print(f"Total Pengeluaran: Rp{total_keluar}")
    print(f"Saldo Akhir: Rp{total_masuk - total_keluar}\n")

def tampilkan_semua(data):
    print("Daftar Transaksi: ")
    for i, transaksi in enumerate(data):
        print(f"{i}. {transaksi['tanggal']} | {transaksi['jenis']} | Rp{transaksi['jumlah']} | {transaksi['kategori']}")
    print()

def update_transaksi(data):
    tampilkan_semua(data)
    nomor_transaksi = int(input("Pilih nomor transaksi yang ingin diubah: "))
    if 0 <= nomor_transaksi < len(data):
        print("Masukkan data baru:")
        data[nomor_transaksi]['tanggal'] = input("Tanggal: ")
        data[nomor_transaksi]['jenis'] = input("Jenis: ")
        data[nomor_transaksi]['jumlah'] = input("Jumlah: ")
        data[nomor_transaksi]['kategori'] = input("Kategori: ")
        print("Transaksi berhasil diubah.\n")
    else:
        print("Nomor tidak valid.\n")

def hapus_transaksi(data):
    tampilkan_semua(data)
    nomor_transaksi = int(input("Pilih nomor transaksi yang ingin dihapus: "))
    if 0 <= nomor_transaksi < len(data):
        data.pop(nomor_transaksi)
        print("Transaksi berhasil dihapus.\n")
    else:
        print("Nomor tidak valid.\n")
