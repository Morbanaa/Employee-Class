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
                break
    
        # Collect Id Number
        while True:
            id_number = input(f"Enter id number #{counter}: ").upper()
            if id_number != "" and id_number != " ":
                break
        
        # Collect Department
        while True:
            department = input(f"Enter department #{counter}: ").upper()
            if department != "" and department != " ":
                break
        
        # Collect Job Title
        while True:
            job_title = input(f"Enter job title #{counter}: ").upper()
            if job_title != "" and job_title != " ":
                break
        
        # Create and store employee objects
        employees.append(Employee(name,id_number,department,job_title))

        # Would user like to add more data
        choice = input("Would you like to make another entry?(Y/N)" ).upper()
        if choice == "Y" or choice == "YES":
            continue
        else:
            break

    # Display table calling employee display method
    for employee in employees:
        employee.display()

if __name__ == "__main__":
    main()

