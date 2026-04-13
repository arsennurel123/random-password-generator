# Random Password Generator 🔐

Простой и мощный генератор случайных паролей на Python с полной настройкой параметров.

## Описание

Этот проект предоставляет удобный инструмент для генерации безопасных случайны�� паролей с различными параметрами и опциями. Вы можете полностью контролировать, какие символы использовать в пароле.

## Возможности ✨

- 🔤 Включение/исключение прописных букв
- 🔡 Включение/исключение строчных букв
- 🔢 Включение/исключение цифр
- 🔣 Включение/исключение специальных символов
- 📏 Настраиваемая длина пароля
- 🚀 Простая и интуитивная API

## Установка

Клонируйте репозиторий:

```bash
git clone https://github.com/arsennurel123/random-password-generator.git
cd random-password-generator
```

Или просто скопируйте файл `password_generator.py` в ваш проект.

**Требования:** Python 3.6+

## Использование

### Базовое использование

```python
from password_generator import generate_password

# Генерировать пароль по умолчанию (12 символов)
password = generate_password()
print(password)  # Например: aB3$xYz9@mK2
```

### Настройка длины пароля

```python
# Генерировать пароль из 20 символов
password = generate_password(length=20)
print(password)
```

### Выбор типов символов

```python
# Пароль только из букв и цифр (без специальных символов)
password = generate_password(use_special=False)
print(password)

# Пароль только из строчных букв и цифр
password = generate_password(use_uppercase=False, use_special=False)
print(password)

# Пароль только из букв
password = generate_password(use_digits=False, use_special=False)
print(password)
```

### Примеры

```python
from password_generator import generate_password, generate_multiple_passwords

# Пример 1: Пароль по умолчанию
pwd1 = generate_password()
print(f"Пароль (12 символов): {pwd1}")

# Пример 2: Короткий пароль
pwd2 = generate_password(length=8)
print(f"Пароль (8 символов): {pwd2}")

# Пример 3: Сильный пароль
pwd3 = generate_password(length=20)
print(f"Сильный пароль: {pwd3}")

# Пример 4: Несколько паролей за раз
passwords = generate_multiple_passwords(count=5, length=12)
for i, pwd in enumerate(passwords, 1):
    print(f"{i}. {pwd}")
```

## API Документация

### `generate_password()`

Генерирует один случайный пароль.

**Параметры:**
- `length` (int): Длина пароля. По умолчанию: 12
- `use_uppercase` (bool): Использовать прописные буквы (A-Z). По умолчанию: True
- `use_lowercase` (bool): Использовать строчные буквы (a-z). По умолчанию: True
- `use_digits` (bool): Использовать цифры (0-9). По умолчанию: True
- `use_special` (bool): Использовать специальные символы. По умолчанию: True

**Возвращает:**
- `str`: Сгенерированный пароль

**Примеры:**
```python
generate_password()  # 'aB3$xYz9@mK2'
generate_password(length=8)  # 'x9K2@mYz'
generate_password(use_special=False)  # 'aB3xYz9mK2L5'
```

### `generate_multiple_passwords()`

Генерирует несколько паролей.

**Параметры:**
- `count` (int): Количество паролей. По умолчанию: 5
- `**kwargs`: Дополнительные параметры передаются в `generate_password()`

**Возв��ащает:**
- `list`: Список сгенерированных паролей

**Примеры:**
```python
generate_multiple_passwords(count=3)  # ['aB3$xYz9@mK2', 'x9K2@mYzL5P1', 'qW8#eRt4%uIo']
generate_multiple_passwords(count=5, length=20)  # Список из 5 паролей длиной 20 символов
```

## Запуск примеров

Просто запустите скрипт:

```bash
python password_generator.py
```

## Примеры вывода

```
Пароль (12 символов): aB3$xYz9@mK2
Пароль (8 символов): x9K2@mYz
Сильный пароль (20 символов): aB3$xYz9@mK2qW8#eRt4
Пароль (буквы и цифры): aB3xYz9mK2L5qW8eRt4
```

## Безопасность ⚠️

Этот генератор использует модуль `random` Python. Для криптографически безопасной генерации паролей в продакшене рекомендуется использовать модуль `secrets`:

```python
import secrets
import string

password = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(12))
```
## Автор

arsennurel123


