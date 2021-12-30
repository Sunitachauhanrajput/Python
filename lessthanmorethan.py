student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
list_length=len(student_marks)
i=0
less_than50=0
more_than50=0
while i<list_length:
    marks=student_marks[i]
    if marks<50:
        less_than50=less_than50+1
    else:
        more_than50=more_than50+1
print(more_than50)
print(less_than50)