def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result



print(f"Факториал числа 0 равен {factorial(0)}")
print(f"Факториал числа 5 равен {factorial(5)}")
