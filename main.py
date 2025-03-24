def analysis_text(text):
    text = text.lower()
    for punctuation in ".,;:!?(){}[]'\"":
        text = text.replace(punctuation, "")
    words = text.split()
    word_count = len(words)
    longset_word = max(words, key=len)
    vowels = "уеыаоэяию"
    vowel_count = sum(1 for char in text if char in vowels)
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    print(f"Количество слов: {word_count}.")
    print(f"Самое длинное слово: {longset_word}.")
    print(f"Количество гласных в тексте: {vowel_count}")
    print("Частота слов: ")
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency} ")


user_input = input("Введите текст: ")
analysis_text(user_input)
