import random
import string
import random

def generate_password(length=12):
    """Генерация случайного пароля заданной длины."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        password += random.choice(characters)
    return password


# 123


# Пример использования
password_length = 12  # Вы можете выбрать любую длину пароля
print("Ваш новый пароль:", generate_password(password_length))



3