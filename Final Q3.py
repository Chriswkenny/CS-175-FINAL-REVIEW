#Christopher Kenny
#CS 175
#Final Exam Q3
#create a program to count the occurrences of each word in a sentence.

sentence = "apple banana apple orange banana apple"

repeating_words = {}

for word in sentence.split():
    if word in repeating_words:
        repeating_words[word] += 1
    else:
        repeating_words[word] = 1

print(repeating_words)

