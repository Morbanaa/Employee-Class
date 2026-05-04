from classes import Employee

def main():
    employees = [] # Holds list of employee objects

    # Temps Storage Vars
    name = ""
    id_number = ""
    department = ""
    job_title = ""

    counter = 0
    while True:
        counter +=1

        # Collect Name
        while True:
            name = input(f"Enter name #{counter}: ").upper()
            if name != "" and name != " ":
                clear_screen()
                break
        
        # Collect Id Number
        while True:
            id_number = input(f"Enter id number #{counter}: ").upper()
            if id_number != "" and id_number != " ":
                clear_screen()
                break
        
        # Collect Department
        while True:
            department = input(f"Enter department #{counter}: ").upper()
            if department != "" and department != " ":
                clear_screen()
                break
        
        # Collect Job Title
        while True:
            job_title = input(f"Enter job title #{counter}: ").upper()
            if job_title != "" and job_title != " ":
                clear_screen()
                break
        
        # Create and store employee objects
        employees.append(Employee(name,id_number,department,job_title))

        # Would user like to add more data
        choice = input("Would you like to make another entry?(Y/N)" ).upper()
        if choice == "Y" or choice == "YES":
            clear_screen()
            continue
        else:
            clear_screen()
            break

    # Display table calling employee display method
    for employee in employees:
        employee.display()


def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

if __name__ == "__main__":
    main()

