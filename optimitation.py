students_name = ['ion','ana']
def inputname():
    name = input("Student: \n>")
def names():
    for i in range(len(students_name )):
        if students_name[i] == name:
                print(f" >> {students_name}")

inputname()
names()
