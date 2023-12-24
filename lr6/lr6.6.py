text = input("Введите текст: ")
words = text.split()

word_frequency = {} 

for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

for word, frequency in word_frequency.items():
    print(f"Слово {word}, содержится {frequency} раз")
