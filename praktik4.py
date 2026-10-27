# Praktik 4: Sistem Inventaris Barang

inventaris = {
    "Buku": (15000, 10),
    "Pensil": (3000, 20),
    "Penggaris": (5000, 8)
}

def tambah_barang(nama, harga, stok):
    if nama in inventaris:
        print("Barang sudah ada.")
    else:
        inventaris[nama] = (harga, stok)
        print("Barang berhasil ditambahkan.")

def ubah_stok(nama, stok_baru):
    if nama in inventaris:
        harga = inventaris[nama][0]
        inventaris[nama] = (harga, stok_baru)
        print("Stok berhasil diperbarui.")
    else:
        print("Barang tidak ditemukan.")

def cari_rentang_harga(minimum, maksimum):
    print(f"Barang dengan harga {minimum} sampai {maksimum}:")
    ditemukan = False

    for nama, (harga, stok) in inventaris.items():
        if minimum <= harga <= maksimum:
            print(f"{nama}: harga Rp{harga}, stok {stok}")
            ditemukan = True

    if not ditemukan:
        print("Tidak ada barang dalam rentang tersebut.")

def total_nilai_inventaris():
    total = sum(
        harga * stok
        for harga, stok in inventaris.values()
    )
    return total

print("--- Data Inventaris Awal ---")
for nama, (harga, stok) in inventaris.items():
    print(f"{nama}: harga Rp{harga}, stok {stok}")

tambah_barang("Penghapus", 2000, 15)
ubah_stok("Pensil", 25)
cari_rentang_harga(2000, 5000)

print("Total nilai inventaris: Rp", total_nilai_inventaris())
print("Data inventaris akhir:", inventaris)