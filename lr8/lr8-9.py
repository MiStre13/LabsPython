def max_length_word(file):
    with open(file, 'r') as f:
        content = f.read()
        words = content.split()
        max_length = max(len(word) for word in words)
        max_length_words = [word for word in words if len(word) == max_length]
        if len(max_length_words) == 1:
            return max_length_words[0]
        else:
            return max_length_words

filename = "/Users/mikhailstreltsov/Desktop/учеба/pythonProject/lr8/title.txt"
result = max_length_word(filename)
print(result)
