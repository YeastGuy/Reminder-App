import time
from plyer import notification
from datetime import datetime
import sys


def setup():
    SubNum = 0
    while True:
        try:
            while SubNum < 1 or SubNum > 15:
                SubNum = int(input("Write down number of subjects(max 15): "))
            break
        except ValueError:
            print("Please, write a number")
    Teachers = [""] * SubNum
    Subjects = [""] * SubNum

    for x in range(SubNum):
        Temp = input("Subject number " + str(x + 1) + ": ")
        Subjects[x] = Temp
    for x in range(SubNum):
        temp = input("Teacher for " + Subjects[x].lower() + " subject: ")
        Teachers[x] = temp
    file = open("reminders.txt", "w")
    for x in range(SubNum):
        file.write("0000 0000 - " + Subjects[x] + " : " + Teachers[x] + " = " + "\n")
    file.close()
    menu()


def main():
    date = ""
    moment = ""
    k = 0
    file = open("reminders.txt", "r")
    lines = file.readlines()
    file.close()
    Teachers = []
    Subjects = []
    for a in range(len(lines)):
        subject = ""
        teacher = ""
        res = lines[a].split()
        start_subject = res.index("-")
        start_teacher = res.index(":")
        start_rem = res.index("=")
        for b in range(start_subject + 1, start_teacher):
            subject = subject + res[b] + " "
        Subjects.append(subject)

        for c in range(start_teacher + 1, start_rem):
            teacher = teacher + res[c] + " "
        Teachers.append(teacher)
    for x in range(len(lines)):
        print(str(x + 1) + ") " + Subjects[x] + " - " + Teachers[x])
    while True:
        try:
            while k < 1 or k > len(lines):
                k = int(input("Select a subject"))
            break
        except ValueError:
            print("Please, write a number")
    sub = Subjects[k - 1]
    with open("reminders.txt", "r") as check_obj:
        for op in check_obj:
            if sub in op and not"0000" in op:
                print("This subject already has a reminder")
                menu()

    while True:
        try:
            while len(date) > 4 or len(date) < 4:
                date = input("Enter the date (in'MMDD' format, i.e. 11th of june is 0611)")
            break
        except ValueError:
            print("Please, write it in the given format")

    while True:
        try:
            while len(moment) > 4 or len(moment) < 4:
                moment = input("Enter the time (in 'HHMM' format, i.e. 13 o'lock 30 minutes is 1330)")
            break
        except ValueError:
            print("Please write it in 'HHMM' format")
    rem = input("What reminder do you want to set for " + Subjects[k - 1].lower() + " lesson?")
    # updating line
    with open("reminders.txt", "r") as app_obj:
        for line in app_obj:
            if sub in line:
                newline = line.split()
                newline[0] = str(date)
                newline[1] = str(moment)
                newline.append(rem)
                updated_line = ""
                for m in range(len(newline)):
                    updated_line = updated_line + newline[m] + " "
                updated_line = updated_line + "\n"

    # rewriting all the lines, however, replacing the one we need
    f = open("reminders.txt", "w")
    lines[k - 1] = updated_line
    f.writelines(lines)
    f.close()
    menu()


def checking():
    is_reminded = False
    updated_line = ""
    a = 0
    f = open("reminders.txt", "r")
    lines = f.readlines()
    f.close()
    today = time.strftime('%m%d')
    now = datetime.now()
    current_time = now.strftime("%H%M")
    with open("reminders.txt", "r") as read_obj:
        for line in read_obj:
            if today in line and current_time in line:
                subject = ""
                teacher = ""
                reminder = ""
                res = line.split()
                start_subject = res.index("-")
                start_teacher = res.index(":")
                start_rem = res.index("=")

                for x in range(start_subject + 1, start_teacher):
                    subject = subject + res[x] + " "

                for k in range(start_teacher + 1, start_rem):
                    teacher = teacher + res[k] + " "

                for i in range(start_rem + 1, len(res)):
                    reminder = reminder + res[i] + " "

                notification.notify(
                    title=teacher + "is going to beat you at " + subject.lower() + "lesson",
                    message=reminder,
                    timeout=5
                )
                res[0] = "0000"
                res[1] = "0000"
                for b in range(start_rem + 1):
                    updated_line = updated_line + res[b] + " "
                updated_line = updated_line + "\n"
                is_reminded = True
                break
            a += 1
    if is_reminded:
        f = open("reminders.txt", "w")
        lines[a] = updated_line
        f.writelines(lines)
        f.close()




def delete():
    desire = 0
    Subjects = []
    f = open("reminders.txt", "r")
    lines = f.readlines()
    for a in range(len(lines)):
        subject = ""
        res = lines[a].split()
        start_subject = res.index("-")
        start_teacher = res.index(":")
        for b in range(start_subject + 1, start_teacher):
            subject = subject + res[b] + " "
        Subjects.append(subject)
    for c in range(len(lines)):
        print(str(c + 1) + ") " + Subjects[c])
    while True:
        try:
            while desire < 1 or desire > len(lines):
                desire = int(input("What subject do you want to remove? "))
            break
        except ValueError:
            print("Please, write a number")
    lines.pop(desire - 1)
    f.close()

    f = open("reminders.txt", "w")
    f.writelines(lines)
    f.close()
    menu()


def append():
    subject = input("What is the subject you want to add? ")
    teacher = input("What is the teacher for " + subject + " lesson?")
    f = open("reminders.txt", "r")
    lines = f.readlines()
    lines.append("0000 0000 - " + subject + " : " + teacher + " = " + "\n")
    f.close()

    f = open("reminders.txt", "w")
    f.writelines(lines)
    f.close()
    menu()


def reset():
    desire = 0
    Teachers = []
    Subjects = []
    f = open("reminders.txt", "r")
    lines = f.readlines()
    f.close()
    for a in range(len(lines)):
        subject = ""
        teacher = ""
        res = lines[a].split()
        start_subject = res.index("-")
        start_teacher = res.index(":")
        start_rem = res.index("=")
        for b in range(start_subject + 1, start_teacher):
            subject = subject + res[b] + " "
        Subjects.append(subject)
        for k in range(start_teacher + 1, start_rem):
            teacher = teacher + res[k] + " "
        Teachers.append(teacher)
    for c in range(len(lines)):
        print(str(c + 1) + ") " + Subjects[c])
    while True:
        try:
            while desire < 1 or desire > len(lines):
                desire = int(input("What subject do you want to remove? "))
            break
        except ValueError:
            print("Please, write a number")
    lines[desire - 1] = "0000 0000 - " + Subjects[desire - 1] + " : " + Teachers[desire - 1] + " = " + "\n"
    f = open("reminders.txt", "w")
    f.writelines(lines)
    f.close()
    menu()


def menu():
    choice = 0
    print("1) Getting started")
    print("2) Add a reminder")
    print("3) Delete a reminder")
    print("4) Add a lesson")
    print("5) Delete a lesson")
    print("6) Quit")
    while True:
        try:
            while choice < 1 or choice > 6:
                choice = int(input("Select an option"))
            break
        except ValueError:
            print("Please write a value")
    if choice == 1:
        setup()
    elif choice == 2:
        main()
    elif choice == 3:
        reset()
    elif choice == 4:
        append()
    elif choice == 5:
        delete()
    else:
        sys.exit()


checking()
if __name__ == "__main__":
    menu()
