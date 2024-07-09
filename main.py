from Module_1.alphabet import *
from Module_1.valid import valid_lang, valid_cipher, valid_step, cipher_text
from Module_1.cipher import caesar_shift


def caesar_cipher():

    lang = valid_lang()
    choice = valid_cipher()
    step = valid_step()
    text = cipher_text()

    step = step if choice in ["шифровать", "encrypt"] else -step

    if lang == "r":
        result = caesar_shift(text, step, rus_upper_alphabet, rus_lower_alphabet)
        print("Результат:", result)
    else:
        result = caesar_shift(text, step, ascii_uppercase, ascii_lowercase)
        print("Result:", result)


if __name__ == "__main__":
    caesar_cipher()
