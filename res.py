def percentage(total_marks, subjects):
    return total_marks / subjects

name = input("Student Name: ")

math = int(input("Math: "))
science = int(input("Science: "))
english = int(input("English: "))
socialscience = int(input("Social Science: "))
gk = int(input("G K: "))
sports = int(input("Sports: "))

total = math + science + english + socialscience + gk + sports
print("\nStudent:", name)
print("Total:", total)
print("Percentage:", percentage(total, 6))