def text_punctuation(text):
    for punctuation in ".,;:!?(){}[]'\"":
        text = text.replace(punctuation, "")
    return text


def long_word(text):
    words = text.split()
    return max(words, key=len)


def vowels(text):
    vowels = "уеыаоэяию"
    return sum(1 for char in text if char in vowels)


def word_frequency(text):
    word_frequency = {}
    words = text.split()
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency


user_input = input("Введите текст: ")
redact_text = text_punctuation(user_input).lower()
print(f"Количество слов: {len(redact_text.split())}.")
print(f"Самое длинное слово: {long_word(redact_text)}.")
print(f"Количество гласных в тексте: {vowels(redact_text)}")
print("Частота слов: ")
for word, frequency in word_frequency(redact_text).items():
    print(f"{word}: {frequency} ")
