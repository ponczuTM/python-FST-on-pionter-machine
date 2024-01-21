import random

def generate_numbers():
    numbers = []
    for _ in range(1000):
        number = random.randint(-10000, 10000)
        while number == 0:
            number = random.randint(-10000, 10000)
        numbers.append(number)
    return numbers

def write_to_file(numbers, filename):
    with open(filename, 'w') as file:
        file.write(', '.join(map(str, numbers)))

if __name__ == "__main__":
    generated_numbers = generate_numbers()
    write_to_file(generated_numbers, 'input.txt')