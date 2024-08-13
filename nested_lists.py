#Find the students with the second lowest grade

if __name__ == '__main__':
    records = []
    second_lowest_students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())    
        records.append([name, score])

    scores = [record[1] for record in records]

    
    for record in records: 
        if record[1] == sorted(set(scores))[1]:
            second_lowest_students.append(record[0])
    
    second_lowest_students.sort()

    for student in second_lowest_students:
        print(student)