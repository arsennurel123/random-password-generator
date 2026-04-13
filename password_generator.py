import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    lowercase = string.ascii_lowercase if use_lowercase else ''
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special = string.punctuation if use_special else ''

    all_characters = lowercase + uppercase + digits + special

    if not all_characters:
        raise ValueError('At least one character type must be selected.')

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# Example usage
if __name__ == '__main__':
    print(generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True))