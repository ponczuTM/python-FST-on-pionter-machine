import random

# Tworzymy pustą listę, do której będziemy dodawać wygenerowane liczby
unique_numbers = []

# Definiujemy funkcję do generowania unikalnych liczb w podanym przedziale
def generate_unique_numbers(num_numbers, min_range, max_range):
    while len(unique_numbers) < num_numbers:
        num = random.randint(min_range, max_range)
        if num != 0 and num not in unique_numbers:
            unique_numbers.append(num)

# Generujemy 10 000 unikalnych liczb z przedziału -100 000 do 100 000
generate_unique_numbers(10000, -100000, 100000)

# Zapisujemy wygenerowane liczby do pliku
with open("output_prezka.txt", "w") as file:
    for num in unique_numbers:
        file.write(f"{int(num)}, ")

print("Wygenerowano i zapisano 10 000 unikalnych liczb do pliku 'output_prezka.txt'.")
