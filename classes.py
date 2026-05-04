class Employee():
    def __init__(self,name,id_number,department,job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title

    def display(self):
        print(f"{self.name} {self.id_number} {self.department} {self.job_title}")
