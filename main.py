# Удалить все пробелы из строки, чтобы игнорировать их при проверке.
# Привести строку к нижнему регистру, чтобы игнорировать регистр символов.
# Сравнить строку с её обратной версией.
# Если строка и её обратная версия совпадают, то строка является палиндромом.
# Если строка и её обратная версия не совпадают, то строка не является палиндромом.

def is_palindrome(s):
    s = s.replace(" ", "")
    s = s.lower()
    if s == s[::-1]:
        return True
    return False

print(is_palindrome("А роза упала на лапу Азора"))  # True
print(is_palindrome("Hello world"))                # False
print(is_palindrome("12321"))                      # True
print(is_palindrome("No lemon, no melon"))         # True