#Christopher Kenny
#CS 175
#Final Exam Q1
#Type the lines of code that calls the split method to print only the year part of the variable "date_string"

date_string = '11/26/2020'

date_string_1 = date_string.split('/')

for i in range(len(date_string_1)):
    date_string_1[i] = int(date_string_1[i])

print(date_string_1[2])
