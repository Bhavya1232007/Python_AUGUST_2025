student_marks={
    "Jenny":92,
    "Harry":78,
    "Dimpy":56,
    "Rahul":41,
    "Aniket":99,
    "Prem":34
}


def MG(marks):
    if(marks>=91 and marks<=100):
        Grade="A+"
        return Grade
    elif(marks>=81 and marks<=90):
        Grade="A"
        return Grade
    elif(marks>=71 and marks<=80):
        Grade="B+"
        return Grade
    elif(marks>=61 and marks<=70):
        Grade="B"
        return Grade
    elif(marks>=51 and marks<=60):
        Grade="C"
        return Grade
    elif(marks>=41 and marks<=50):
        Grade="D"
        return Grade
    else:
        Grade="F"
        return Grade
student_grade={}
for i in student_marks:
    marks=student_marks[i]
    #print(marks)
    Grade=MG(marks)
    #print(Grade)
    student_grade[i]=Grade
print(student_grade)
