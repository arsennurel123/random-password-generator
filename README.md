# Random Password Generator

Генератор случайных паролей на Python.

## Что это?

Простой скрипт для генерации надежных паролей. Можно выбрать, какие символы использовать - буквы, цифры, спецсимволы.

## Установка

```bash
git clone https://github.com/arsennurel123/random-password-generator.git
cd random-password-generator
```

Нужен Python 3.6+

## Как использовать

```python
from password_generator import generate_password

# Пароль по умолчанию (12 символов)
password = generate_password()
print(password)

# Пароль длиной 20 символов
password = generate_password(length=20)
print(password)

# Без спецсимволов
password = generate_password(use_special=False)
print(password)
```

## Параметры

- `length` - длина пароля (по умолчанию 12)
- `use_uppercase` - большие буквы (по умолчанию включено)
- `use_lowercase` - маленькие буквы (по умолчанию включено)
- `use_digits` - цифры (по умолчанию включено)
- `use_special` - спецсимволы (по умолчанию включено)

## Примеры

```bash
python password_generator.py
```

Выведет несколько сгенерированных паролей:

```
Пароль (12 символов): aB3$xYz9@mK2
Пароль (8 символов): x9K2@mYz
Сильный пароль (20 символов): aB3$xYz9@mK2qW8#eRt4
```

## Автор

arsennurel123