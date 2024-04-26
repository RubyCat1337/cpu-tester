import time
import psutil
from multiprocessing import Pool, cpu_count

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def worker(chunk_size):
    start_time = time.time()
    prime_numbers = []
    num = 2 + chunk_size[0]
    while num <= chunk_size[1]:
        if is_prime(num):
            prime_numbers.append(num)
        num += 2  # Шаг 2, потому что четные числа больше 2 не простые
    return time.time() - start_time

def cpu_test(chunk_size):
    
    print(f"Начало тестирования процессора с {cpu_count()} ядрами...")

    chunk_size = [(i * 10000, (i + 1) * 10000) for i in range(cpu_count())]
    
    with Pool(processes=cpu_count()) as pool:
        times = pool.map(worker, chunk_size)
    
    cpu_usage = psutil.cpu_percent(interval=1, percpu=True)

    print("Тестирование завершено.")
    print("Информация о нагрузке на процессор и времени решения задачи:")
    for i, (cpu, time) in enumerate(zip(cpu_usage, times)):
        print(f"Ядро {i}: {cpu}% загрузки, Время решения задачи: {time} сек")

if __name__ == "__main__":
    test_duration = 10
    cpu_test(test_duration)
