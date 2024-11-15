#Christopher Kenny
#CS 175
#Final Exam Q8
#Create a program to count the number of uppercase letters, lowercase letters, and digits in a string.

text = "Hello World! Python3"
uppercase = 0
lowercase = 0
digits = 0

for char in text:
  if char.isupper():
    uppercase += 1
  elif char.islower():
    lowercase += 1
  elif char.isdigit():
    digits += 1
  else:
    continue

print(f"Uppercase: {uppercase}, Lowercase: {lowercase}, Digits: {digits}")
