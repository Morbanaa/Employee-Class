from classes import Employee

def main():
    employees = []

    name = ""
    id_number = ""
    department = ""
    job_title = ""

    counter = 0
    while True:
        counter +=1
        while True:
            name = input(f"Enter name #{counter}: ").upper()
            if name != "" and name != " ":
                break

        while True:
            id_number = input(f"Enter id number #{counter}: ").upper()
            if id_number != "" and id_number != " ":
                break

        while True:
            department = input(f"Enter department #{counter}: ").upper()
            if department != "" and department != " ":
                break

        while True:
            job_title = input(f"Enter job title #{counter}: ").upper()
            if job_title != "" and job_title != " ":
                break

        choice = input("Would you like to make another entry?(Y/N)" ).upper()
        if choice == "Y" or choice == "YES":
            continue
        else:
            break


if __name__ == "__main__":
    main()

