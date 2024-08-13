from collections import namedtuple
N = int(input())
cols = input().split()
Student = namedtuple('Student', cols)
students = []
for _ in range(N):
    data = input().split()
    student = Student(*data)
    students.append(student)

average_mark = sum(int(student.MARKS) for student in students)/N
print(f"{average_mark: .2f}")



