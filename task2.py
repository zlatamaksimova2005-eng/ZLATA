is_active = True  # Статус активен пользователь или нет
is_blocked = False  # # Статус заблокирован пользователь или нет

if is_active and not is_blocked:
    print("Пользователь прошел проверку")
else:
    print("Пользователь не прошел проверку")

# Тест 1: активен и не заблокирован
is_active = True
is_blocked = False

# Тест 2: активен, но заблокирован
is_active = True
is_blocked = True

# Тест 3: не активен, но не заблокирован
is_active = False
is_blocked = False

# Тест 4: не активен и заблокирован
is_active = False
is_blocked = True
