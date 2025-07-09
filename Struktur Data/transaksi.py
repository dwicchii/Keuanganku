from datetime import datetime

def catat_transaksi(data):
    tanggal = input("Masukkan tanggal (YYYY-MM-DD): ")
    jenis = input("Jenis (pemasukan/pengeluaran): ")
    jumlah = input("Jumlah: ")
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