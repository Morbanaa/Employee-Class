from classes import Employee

def main():
    employees = []

    name = ""
    id_number = ""
    department = ""
    job_title = ""

    while True:
        name = input("Enter your name: ").upper()
        if name != "" and name != " ":
            break

    while True:
        id_number = input("Enter your id number: ").upper()
        if id_number != "" and id_number != " ":
            break

    while True:
        department = input("Enter your department: ").upper()
        if department != "" and department != " ":
            break

    while True:
        job_title = input("Enter your job title: ").upper()
        if job_title != "" and job_title != " ":
            break


if __name__ == "__main__":
    main()

