# Praktik 2: Pengolahan Nilai Mahasiswa

nilai = [85, 92, 78, 65, 90, 55, 35, 72]

def tentukan_grade(n):
    if n >= 85:
        return "A"
    elif n >= 70:
        return "B"
    elif n >= 55:
        return "C"
    elif n >= 40:
        return "D"
    else:
        return "E"

grade_mahasiswa = [tentukan_grade(n) for n in nilai]

frekuensi_grade = {
    "A": grade_mahasiswa.count("A"),
    "B": grade_mahasiswa.count("B"),
    "C": grade_mahasiswa.count("C"),
    "D": grade_mahasiswa.count("D"),
    "E": grade_mahasiswa.count("E")
}

rata_rata = sum(nilai) / len(nilai)

print("--- Hasil Nilai Mahasiswa ---")
print("Daftar nilai:", nilai)
print("Grade setiap mahasiswa:", grade_mahasiswa)
print(f"Rata-rata nilai: {rata_rata:.2f}")
print("Nilai tertinggi:", max(nilai))
print("Nilai terendah:", min(nilai))
print("Frekuensi grade:", frekuensi_grade)