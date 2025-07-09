from collections import defaultdict

def hitung_per_kategori(data):
    kategori_total = defaultdict(int)
    for item in data:
        if item['jenis'] == 'pengeluaran':
            kategori_total[item['kategori']] += int(item['jumlah'])
    return kategori_total

def tampilkan_per_kategori(data):
    kategori_total = hitung_per_kategori(data)
    print("\n=== Pengeluaran per Kategori ===")
    for kategori, total in kategori_total.items():
        print(f"{kategori}: Rp{total}")
    print()
