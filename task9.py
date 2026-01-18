def is_palindrome(s):

    s_lower = s.lower()

    s_clean = ''.join(s_lower.split())

    return s_clean == s_clean[::-1]

print(is_palindrome("радар"))
print(is_palindrome("Мадам"))
print(is_palindrome("А роза упала на лапу Азора"))
print(is_palindrome("Привет"))
