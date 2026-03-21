# Average of Marks in 5 Subjects

math = int(input('Enter the marks of math: '))
physics = int(input('Enter the marks of physics: '))
chemistry = int(input('Enter the marks of chemistry: '))
Hindi = int(input('Enter the marks of Hindi: '))
English = int(input('Enter the marks of English: '))

total_marks = math+physics+chemistry+Hindi+English
average_marks = (math+physics+chemistry+Hindi+English)/5

print(f'Total marks is: {total_marks} and average marks is: {average_marks}')