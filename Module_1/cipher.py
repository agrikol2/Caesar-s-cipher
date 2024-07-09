def caesar_shift(text, step, alphabet_upper, alphabet_lower):

    result = ""
    for char in text:
        if char in alphabet_upper:
            new_index = (alphabet_upper.index(char) + step) % len(alphabet_upper)
            result += alphabet_upper[new_index]
        elif char in alphabet_lower:
            new_index = (alphabet_lower.index(char) + step) % len(alphabet_lower)
            result += alphabet_lower[new_index]
        else:
            result += char
    return result
