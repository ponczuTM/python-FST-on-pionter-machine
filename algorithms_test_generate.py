import mroczkowski_library as mo
import time

# Rozpocznij pomiar czasu
start_time = time.time()

i=0
a=1
while i<20000:
    print(i)
    i+=1
# Zakończ pomiar czasu
end_time = time.time()

# Oblicz czas trwania obliczeń
elapsed_time = end_time - start_time

# Wyświetl wynik i czas wykonania
print(f"Wynik: {a}")
print(f"Czas wykonania: {elapsed_time} sekund")



