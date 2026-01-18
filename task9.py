def is_lucky_number(num: int) -> bool:

    if not (100000 <= num <= 999999):
        raise ValueError("Число не является шестизначным положительным числом")

    digits = [int(d) for d in str(num)]


    sum_first = sum(digits[:3])

    sum_last = sum(digits[3:])

    return sum_first == sum_last


print(is_lucky_number(123321))
print(is_lucky_number(111111))
print(is_lucky_number(123456))
print(is_lucky_number(456243))
