sentence = input("Enter a sentence: ")

sentence = sentence.lower()

sentence = sentence.replace(".", "")
sentence = sentence.replace(",", "")
sentence = sentence.replace("!", "")
sentence = sentence.replace("?", "")

words = sentence.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1

print("Word frequencies:")

for word in frequency:
    print(word + ":", frequency[word])

highest_count = max(frequency.values())

most_frequent = []

for word in frequency:
    if frequency[word] == highest_count:
        most_frequent.append(word)

print("Most frequent word(s):", ", ".join(most_frequent))
print("Total words:", len(words))
print("Unique words:", len(frequency))

