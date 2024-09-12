
import csv
timetable =  [["---","---","---","---","---", "---"],
              ["---","---","---","---","---", "---"],
              ["---","---","---","---","---","---"],
              ["---","---","---","---","---", "---"], 
              ["---","---","---","---","---", "---"]]

def menu(timetable):
    print("Choose one:\n1. Output Timetable\n2. Edit lesson\n3. Load\n4. Save\n5. Close")
    menuChoice = int(input())
    if menuChoice == 1:
        output()
    if menuChoice == 2:
        editLesson(timetable)
    if menuChoice == 3:
        print("it never said i needed to actually program this")
        menu(timetable)
    if menuChoice == 4:
        save(timetable)
    if menuChoice == 5:
        exit()

def output():
    for row in timetable:
        for col in row:
            print(col, end=" ")
        print()
    menu(timetable)

def editLesson(timetable):
    print("Enter day (1-5):")
    dayEdit = (int(input())) - 1
    if dayEdit not in range(0,4):
        editLesson()
    print("Enter lesson (1-6):")
    lessonEdit = (int(input())) - 1
    if lessonEdit not in range(0, 5):
        editLesson()
    print("Enter updated lesson:")
    lesson = input()
    timetable[lessonEdit][dayEdit] = subjectCode(lesson)
    print("Updated")
    menu(timetable)

def subjectCode(subjecto):
    subjecto = subjecto.upper()
    if subjecto.__len__() > 3:
        subjecto = subjecto[0] + subjecto[1] + subjecto[2]
    elif subjecto.__len__() < 3:
        subjecto = subjecto + (" " * (3 - subjecto.__len__()))
    return subjecto

def save(timetable):
    with open("timetable.csv", "w+") as timetable1:
        csvWriter = csv.writer(timetable1, delimiter=',')
        csvWriter.writerows(timetable)
        menu()

menu(timetable)