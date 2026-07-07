marks = []

for i in range(5):

    mark = int(input(f"Enter Subject {i+1} Marks: "))
    marks.append(mark)

print("\nMarks =", marks)

print("Total =", sum(marks))

print("Average =", sum(marks)/len(marks))

print("Highest =", max(marks))

print("Lowest =", min(marks))