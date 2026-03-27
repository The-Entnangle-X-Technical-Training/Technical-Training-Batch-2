problem18 = 'hello 18th problem'
print(problem18)#  Average of Marks in 5 Subjects

math = int(input('Enter math marks : '))
eng = int(input('Enter English marks : '))
gk = int(input('Enter GK marks : '))
hindi = int(input('Enter Hindi marks : '))
science = int(input('Enter science marks : '))

total_marks = math + eng +gk + hindi + science

avg_marks = total_marks/5

print(f"Total makrs obtained : {total_marks}\nAverage marks : {avg_marks}")