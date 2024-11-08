import numpy as np  # Import NumPy library

# Fungsi untuk menghitung AB dan AC menggunakan NumPy
def calculate_with_numpy(A, B, C):
    # Mengalikan A dan B
    AB = np.dot(A, B)
    # Mengalikan A dan C
    AC = np.dot(A, C)
    # Menjumlahkan AB dan AC
    result = AB + AC
    return AB, AC, result

# Fungsi untuk menghitung AB dan AC tanpa menggunakan library
def calculate_without_numpy(A, B, C):
    # Hitung AB
    AB = [[0, 0], 
          [0, 0]]

    # Melakukan perkalian A dan B
    for i in range(2):  # Loop untuk baris A
        for j in range(2):  # Loop untuk kolom B
            for k in range(3):  # Loop untuk kolom A dan baris B
                AB[i][j] += A[i][k] * B[k][j]

    # Hitung AC
    AC = [[0, 0], 
          [0, 0]]

    # Melakukan perkalian A dan C
    for i in range(2):  # Loop untuk baris A
        for j in range(2):  # Loop untuk kolom C
            for k in range(3):  # Loop untuk kolom A dan baris C
                AC[i][j] += A[i][k] * C[k][j]

    # Hitung (AB + AC)
    result = [[0, 0], 
              [0, 0]]

    # Melakukan penjumlahan AB dan AC
    for i in range(2):
        for j in range(2):
            result[i][j] = AB[i][j] + AC[i][j]

    return AB, AC, result

# Definisikan matriks A, B, dan C
A = [[2, 0, -3], 
     [1, 4, 5]]

B = [[3, 1], 
     [-1, 0], 
     [4, 2]]

C = [[4, 7], 
     [2, 1], 
     [1, -1]]

# Menghitung menggunakan NumPy
AB_numpy, AC_numpy, result_numpy = calculate_with_numpy(A, B, C)

# Menghitung tanpa NumPy
AB_manual, AC_manual, result_manual = calculate_without_numpy(A, B, C)

# Tampilkan hasil dari NumPy
print("Hasil menggunakan NumPy:")
print("AB =")
print(AB_numpy)

print("AC =")
print(AC_numpy)

print("(AB + AC) =")
print(result_numpy)

# Tampilkan hasil dari manual
print("\nHasil tanpa menggunakan NumPy:")
print("AB =")
print(AB_manual)

print("AC =")
print(AC_manual)

print("(AB + AC) =")
print(result_manual)