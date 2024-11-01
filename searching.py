# Tugas Searching

numbers = [6, 10, 8, 2, 2, 4, 1, 2, 2, 3, 5, 3, 5, 4, 5, 10, 9, 5, 1, 10]

def search_index(input_number):
    if input_number % 2 == 1:
        return "Data ganjil tidak diterima!"
    else:
        indices = [i for i, number in enumerate(numbers) if number == input_number]
        return f"Angka {input_number} ditemukan di indeks : {indices}" if indices else "Angka tidak ditemukan."

try:
    user_input = int(input("Masukkan angka antara 1-10 : "))
    print(search_index(user_input))
except ValueError:
    print("Input tidak valid. Harap masukkan angka antara 1-10.")