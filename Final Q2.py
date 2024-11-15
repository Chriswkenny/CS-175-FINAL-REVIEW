#Christopher Kenny
#CS 175
#Final Exam Q2
#Create a program to multiply each element of 'a' with the corresponding element in 'b' and sum the result. If an element in a is 0, we skip that element.

a = [1, 2, 0, 1]
b = [3, 4, 6, 5]
total = 0

for x in a:
  if x == 0:
    continue
  total += x * b[a.index(x)]

print(total)
