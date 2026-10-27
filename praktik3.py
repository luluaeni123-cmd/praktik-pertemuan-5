# Praktik 3: Operasi Set Penerima Beasiswa

kelompok_a = [101, 102, 103, 104, 105]
kelompok_b = [103, 104, 106, 107]

set_a = set(kelompok_a)
set_b = set(kelompok_b)

irisan = set_a & set_b
hanya_a = set_a - set_b
gabungan = set_a | set_b

print("--- Hasil Operasi Set ---")
print("Kelompok A:", sorted(set_a))
print("Kelompok B:", sorted(set_b))
print("Penerima di kedua kelompok:", sorted(irisan))
print("Hanya di kelompok A:", sorted(hanya_a))
print("Gabungan kedua kelompok:", sorted(gabungan))