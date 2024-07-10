def valid_lang() -> str:
    while True:
        lang_choice = input(
            "Выберете язык/Choose language: R = русский, E = english: "
        ).lower()
        if lang_choice not in ["r", "e"]:
            print(
                "Вы ввели не верно. Ведите один из вариантов ответа/You entered incorrectly. Enter one of the answer options"
            )
        else:
            return lang_choice


lang = valid_lang()


def valid_cipher() -> str:
    while True:
        if lang == "r":

            cipher_choice = input(
                "Введите что будем делать: Шифровать или Дешифровать ? "
            ).lower()
            if cipher_choice not in ["шифровать", "дешифровать"]:
                print("Вы ввели не верно. Ведите один из вариантов ответа")
            else:
                return cipher_choice

        else:
            cipher_choice = input(
                "Enter what we will do: Encrypt or Decrypt ? "
            ).lower()
            if cipher_choice not in ["encrypt", "decrypt"]:
                print("You entered incorrectly. Enter one of the answer options")
            else:
                return cipher_choice


choice = valid_cipher()


def valid_step() -> int:
    while True:
        if lang == "r":
            try:
                step_choice = int(
                    input("На сколько символов будем сдвигать ? Введите число: ")
                )
                return step_choice
            except ValueError:
                print("Вы ввели символ, а не число ")
        else:
            try:
                step_choice = int(
                    input("How many characters will we shift ? Enter the number:")
                )
                return step_choice
            except ValueError:
                print("Enter a number, not a character: ")


steps = valid_step()


def cipher_text() -> str:
    if lang == "r":
        text_cipher = ""
        if choice == "шифровать":
            text_input_cip = input("Введите текст, который хотите зашифровать: ")
            text_cipher += text_input_cip
            return text_input_cip

        else:
            text_input_decip = input("Введите текст, который хотите дешифровать: ")
            return text_input_decip
    else:
        if choice == "Encrypt":
            text_input_cip = input("Enter the text you want to encrypt: ")
            return text_input_cip

        else:
            text_input_decip = input("Enter the text you want to decrypt: ")
            return text_input_decip


text = cipher_text()
