def get_list_number_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

print(get_list_number_divisors(23))
print(get_list_number_divisors(2 ** 16))
