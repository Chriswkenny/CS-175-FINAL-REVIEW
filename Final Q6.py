#Christopher Kenny
#CS 175
#Final Exam Q6
#Create a program to find the longest word in a given sentence.
sentence = "Chicago is very different from Boston"

longest_word = ""

for word in sentence.split():
    if len(word) > len(longest_word):
        longest_word = word

print(longest_word)
