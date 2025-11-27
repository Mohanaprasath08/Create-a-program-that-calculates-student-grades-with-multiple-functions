
def get_marks():
    marks = []
    n = int(input("Enter number of subjects: "))
    for i in range(n):
        mark = float(input(f"Enter mark for subject {i+1}: "))
        marks.append(mark)
    return marks


def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def display_results(name, marks, avg, grade):
    print("\n---- Student Report ----")
    print("Name:", name)
    print("Marks:", marks)
    print("Average:", avg)
    print("Grade:", grade)


def main():
    name = input("Enter student name: ")
    marks = get_marks()
    avg = calculate_average(marks)
    grade = calculate_grade(avg)
    display_results(name, marks, avg, grade)

main()
