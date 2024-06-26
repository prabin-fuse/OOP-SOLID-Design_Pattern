import logging

logging.basicConfig(level=logging.DEBUG)

class University:
    
    def __init__(self, name, location):
        self.__name = name
        self.__location = location
        self.__departments = []

    ## getters:
    @property
    def name(self):
        return self.__name

    @property
    def location(self):
        return self.__location

    @property
    def departments(self):
        return self.__departments

    ## setters:
    @name.setter
    def name(self, name):
        self.__name = name
    
    @location.setter
    def location(self, location):
        self.__location = location
    
    ### add remove departments:
    def add_department(self, department):
        if department not in self.__departments:
            self.__departments.append(department)

    def remove_department(self, department):
        if department in self.__departments:
            self.__departments.remove(department)

    ##diaplay deatils;
    def display_details(self):
        return "Name : {}\n Location : {}\nDepartments : {}".format(self.__name, self.__location,
                                                                    [x for x in self.__departments])



class Department(University):

    def __init__(self, d_name, hod):
        self.department_name = d_name
        self.hod = hod
        self.courses = []

    @property
    def get_department_name(self):
        return self.department_name
    
    @property
    def head_of_department(self):
        return self.hod
    
    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
    
    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)

    def display_details(self):
        return "Department Name : {}\n HOD : {}\Courses : {}".format(self.department_name, self.hod,
                                                                    [x for x in self.courses])

## testing:
uni1 = University("Tribhuwan University", "Kirtipur")

uni1.__name = "Pokhara University" # cannot change bcz of encapulation
print(uni1.name)
uni1.name = "Kathmandu University" ## can be changed because of setter
print(uni1.name)

depart1 = Department("Computer", "KCD")
depart2 = Department("Electronics", "Ramesh")
depart3 = Department("Civil", "Ujjwal")

depart1.add_course("DSA")
depart1.add_course("Discrete Structure")
depart1.add_course("C Programming")

uni1.add_department(depart1)
uni1.add_department(depart2)

print("Uni INfo:\n", uni1.display_details())
print("Department INfo:\n", depart1.display_details())

