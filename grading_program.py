# 1. Create students score dictionary.
students_score = {}

# 2. Input student's name and check if input is correct. (Alphabet, period, and blank only.)

#   2.1 Creat a function that evaluate the validity of name.
def check_name(name):
    #   2.1.1 Remove period and blank and check it if the name is comprised with only Alphabet.
    #   2.1.1.1 Make a list of spelling in the name.
    list_of_spelling = list(name)
    #   2.1.1.2 Remove period and blank from the list.
    while "." in list_of_spelling:
        list_of_spelling.remove(".")
    while " " in list_of_spelling:
        list_of_spelling.remove(" ")

    #   2.1.1.3 Convert the list to a string.
    list_to_string = ""
    list_to_string = list_to_string.join(list_of_spelling)

    #   2.1.1.4 Return if the string is Alphabet.
    return list_to_string.isalpha()


while True:
    #   2.2 Input student's name.
    name = input("Please input student's name. \n")
    check_name(name)
    #   2.3 Check if the name is alphabet. If not, ask to input correct name again.
    while check_name(name) != True:
        name = input("Please input student's name. (Alphabet and period only.)\n")

    # 3. Input student's score and check if input is correct. (digits only and between zero and 100)
    score = input(f"Please input {name}'s score.(0 ~ 100)\n")
    while score.isdigit() == False or int(score) not in range(0, 101):
        score = input("Please input valid numbers only.(Number from zero to 100.)\n")
    students_score[name] = score
    # 4. Ask another student's information.
    another_student = input(
        "Do you want to input another student's information as well? (Y/N)\n"
    )
    while another_student.lower() not in ("yes", "y", "n", "no"):
        #   4.1 Check if the input is valid.
        another_student = input("Please input Y/N only.\n")
    if another_student.lower() in ("yes", "y"):

        continue
    elif another_student.lower() in ("no", "n"):

        break
for student in students_score:
    score = students_score[student]
    score = int(score)
    if score >= 90:
        students_score[student] = "A"
    elif score in range(70, 90):
        students_score[student] = "B"
    elif score in range(50, 70):
        students_score[student] = "C"
    elif score in range(40, 50):
        students_score[student] = "D"
    else:
        students_score[student] = "F"
print(students_score)
