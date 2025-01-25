import time

time_initial = time.time()

def soma1(n):
    soma = 0
    for i in range(n + 1):
        soma += i
    return soma

time_final = time.time()
print(f'O código demorou {time_final - time_initial} segundos')


time_initial = time.time()
def soma2(n):
    return (n * 11) / 2

time_final = time.time()
print(f'O código demorou {time_final - time_initial} segundos')