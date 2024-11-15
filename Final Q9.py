#Christopher Kenny
#CS 175
#Final Exam Q9
#Create a program to check if two strings are anagrams of each other (contain the same characters in a different order).

str1 = "listen"
str2 = "silent"

if sorted(str1) == sorted(str2):
  print("Anagram")
else:
  print("Not Anagram")
