words = input("Введите текст: ").split()

word_lengths = {} 

for word in words:
    word_lengths[word] = len(word)

longest_word = max(word_lengths, key=word_lengths.get)

print("Самое длинное слово:", longest_word)
