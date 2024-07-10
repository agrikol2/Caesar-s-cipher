from Module_1.alphabet import *
from Module_1.valid import *
from Module_1.cipher import caesar_shift


def caesar_cipher():

    step = steps if choice in ["шифровать", "encrypt"] else -steps

    if lang == "r":
        result = caesar_shift(text, step, rus_upper_alphabet, rus_lower_alphabet)
        print("Результат:", result)
    else:
        result = caesar_shift(text, step, ascii_uppercase, ascii_lowercase)
        print("Result:", result)


if __name__ == "__main__":
    caesar_cipher()
