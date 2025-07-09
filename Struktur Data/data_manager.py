import csv

FILE_NAME = 'data_keuangan.csv'

def load_data():
    try:
        with open(FILE_NAME, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(FILE_NAME, mode='w', newline='') as file:
        fieldnames = ['tanggal', 'jenis', 'jumlah', 'kategori']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)