from collections import Counter

# --- Шифр Цезаря ---


def caesar_encrypt(key, plaintext):
    """Шифрование текста с использованием шифра Цезаря."""
    return ''.join([chr((ord(char) + key) % 65536) for char in plaintext])


def caesar_decrypt(key, ciphertext):
    """Дешифрование текста, зашифрованного шифром Цезаря."""
    return ''.join([chr((ord(char) - key) % 65536) for char in ciphertext])


def caesar_crack(ciphertext):
    """Взлом шифра Цезаря с использованием частотного анализа."""
    freq = Counter(ciphertext)
    most_common_char = freq.most_common(1)[0][0]  # Наиболее частый символ
    key = (ord(most_common_char) - ord(' ')) % 65536  # Предполагаем, что это пробел
    return caesar_decrypt(key, ciphertext), key

# --- Шифр Вижинера ---


def vigenere_encrypt(key, plaintext):
    """Шифрование текста с использованием шифра Вижинера."""
    extended_key = (key * ((len(plaintext) // len(key)) + 1))[:len(plaintext)]
    return ''.join([chr((ord(p) + ord(k)) % 65536) for p, k in zip(plaintext, extended_key)])


def vigenere_decrypt(key, ciphertext):
    """Дешифрование текста, зашифрованного шифром Вижинера."""
    extended_key = (key * ((len(ciphertext) // len(key)) + 1))[:len(ciphertext)]
    return ''.join([chr((ord(c) - ord(k)) % 65536) for c, k in zip(ciphertext, extended_key)])

# --- Шифр Вернама ---


def vernam_encrypt(key, plaintext):
    """Шифрование текста с использованием шифра Вернама (XOR)."""
    extended_key = (key * ((len(plaintext) // len(key)) + 1))[:len(plaintext)]
    return ''.join([chr(ord(p) ^ ord(k)) for p, k in zip(plaintext, extended_key)])


def vernam_decrypt(key, ciphertext):
    """Дешифрование текста, зашифрованного шифром Вернама (XOR)."""
    return vernam_encrypt(key, ciphertext)  # XOR обратен сам себе

# --- Основная программа ---


if __name__ == "__main__":
    print("Выберите задание:")
    print("1. Шифр Цезаря (шифрование и дешифрование)")
    print("2. Взлом шифра Цезаря")
    print("3. Шифр Вижинера")
    print("4. Шифр Вернама")
    choice = input("Введите номер задания: ")

    if choice == "1":
        key = int(input("Введите ключ (целое число): "))
        plaintext = input("Введите текст для шифрования: ")
        ciphertext = caesar_encrypt(key, plaintext)
        print("Зашифрованный текст:", ciphertext)
        decrypted_text = caesar_decrypt(key, ciphertext)
        print("Расшифрованный текст:", decrypted_text)

    elif choice == "2":
        ciphertext = input("Введите зашифрованный текст для взлома: ")
        cracked_text, found_key = caesar_crack(ciphertext)
        print("Взломанный текст:", cracked_text)
        print("Найденный ключ:", found_key)

    elif choice == "3":
        key = input("Введите ключ (строка): ")
        plaintext = input("Введите текст для шифрования: ")
        ciphertext = vigenere_encrypt(key, plaintext)
        print("Зашифрованный текст:", ciphertext)
        decrypted_text = vigenere_decrypt(key, ciphertext)
        print("Расшифрованный текст:", decrypted_text)

    elif choice == "4":
        key = input("Введите ключ (строка): ")
        plaintext = input("Введите текст для шифрования: ")
        ciphertext = vernam_encrypt(key, plaintext)
        print("Зашифрованный текст:", ciphertext)
        decrypted_text = vernam_decrypt(key, ciphertext)
        print("Расшифрованный текст:", decrypted_text)

    else:
        print("Неверный выбор задания!")
