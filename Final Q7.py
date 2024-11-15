#Christopher Kenny
#CS 175
#Final Exam Q7
#Create a program to remove all numeric characters from a string.

text = "Python 3.9 is great for 2024!"

new_text = ""

nums = '0123456789'

for char in text:
  if char not in nums:
    new_text += char

print(new_text)
