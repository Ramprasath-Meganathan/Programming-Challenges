studentDetails = {}
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    studentDetails[name] = score

minValue=minvalue2 =0
for value in studentDetails.values():
    if minValue==0:
        minValue=value
    if value==minValue or value==minvalue2:
        continue
    elif value>minValue:
         minvalue2=value     
    else:
        minValue2=minValue
        minValue=value
     

finalList=[]
for key,value in studentDetails.items():
    if(value==minvalue2):
        finalList.append(key)
finalList.sort()
for name in finalList:
    print(name)

# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Example

# The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

# alpha
# beta
# Input Format

# The first line contains an integer, , the number of students.
# The  subsequent lines describe each student over  lines.
# - The first line contains a student's name.
# - The second line contains their grade.

# Constraints

# There will always be one or more students having the second lowest grade.
# Output Format

# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.