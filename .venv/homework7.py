grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

grades_assigned = {}
count = 0
for name in sorted(list(students)):
    grades_assigned[name] = str((sum(grades[count]) / len(grades[count])))[0:4]
    count += 1

print(grades_assigned)



