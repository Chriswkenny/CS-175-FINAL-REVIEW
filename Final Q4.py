#Christopher Kenny
#CS 175
#Final Exam Q4
#Create a program to replace all vowels in a string with the @ character.

text = "Hello, World!"
new_text = text
vowels = "aeiouAEIOU"

for char in vowels:
  new_text = new_text.replace(char, "@")

print(new_text)
