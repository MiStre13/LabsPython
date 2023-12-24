words = input("Введите текст: ").split()

word_counts = {} 

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print("Самое часто встречающееся слово:", max(word_counts, key=word_counts.get))
