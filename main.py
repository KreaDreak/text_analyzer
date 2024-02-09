import string

text = input("Введите текст: ")


punctuation = string.punctuation

for i in range(len(punctuation)):
    text = text.replace(punctuation[i], ' ')

text = text.lower()


words = text.split()

print("Количество разных слов:", len(set(words)))


word_frequency = {}

for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1
print('Частота слов:')
for word, frequency in word_frequency.items():
    print(f'{word}: {frequency}')
