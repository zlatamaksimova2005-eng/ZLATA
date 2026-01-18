number = 2342354235235

list_digits = [int(d) for d in str(number)]

print(sum(list_digits))

print(sum(d for d in list_digits if d % 2 == 0))

print(len(list_digits))

print(min(list_digits))

print(list_digits[0] - list_digits[-1])


