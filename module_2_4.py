numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []      # пустой список
not_primes = []  # пустой список
numbers.remove(1)   # сразу исключаю 1, т.к. число не относится ни к одному из нужных типов
for number in numbers:   # перебираем каждое число в заданном списке numbers
    is_prime = True  # должна быть инициализирована до начала проверки делителей
    for i in range(2, number):  # переберем делители от 2 до number-, т.к. 1 не относится ни к тому ни к другому типу
       if number % i == 0:   # делится ли number на i без остатка
           is_prime = False # если найден делитель, то это уже не простое число
           break  # число найдено, вложенный цикл прервем
    if is_prime:
           primes.append(number)  # если число простое то добавлюем его в список primes
    else:
        not_primes.append(number)  # иначе это непростое число - закидываем его в not_primes
print("Простые числа:", primes)
print("Не простые числа:", not_primes)