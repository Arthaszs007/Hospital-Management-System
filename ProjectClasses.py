#Programmed by Jiho Lee, Qiyuan Liu, Nengji Li
#2023-04-26

#The code has two classes 'Doctor' and 'DoctorManager'
class Doctor: 
    #constructor
    def __init__(self, doctor_id= 0, doctor_name= '', specialization= '', working_time='', qualification='', room_number=0):
        self.doctor_id = doctor_id
        self.doctor_name = doctor_name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number
    
    #getters
    def get_doctor_id(self):
        return self.doctor_id
    
    def get_doctor_name(self):
        return self.doctor_name
    
    def get_specialization(self):
        return self.specialization
    
    def get_working_time(self):
        return self.working_time
    
    def get_qualification(self):
        return self.qualification
    
    def get_room_number(self):
        return self.room_number
    
    #setter
    def set_doctor_id(self, doctor_id):
        self.doctor_id = doctor_id
    
    def set_doctor_name(self, doctor_name):
        self.doctor_name = doctor_name

    def set_specialization(self, specialization):
        self.specialization = specialization

    def set_working_time(self, working_time):
        self.working_time = working_time

    def set_qualification(self, qualification):
        self.qualification = qualification

    def set_room_number(self, room_number):
        self.room_number = room_number

    def __str__(self):
        return f"{self.doctor_id}\t{self.doctor_name}\t{self.specialization}\t{self.working_time}\t{self.qualification}\t{self.room_number}\n"

#This class is used to manage doctors in hospital. It has methods for adding, searching, displaying, editing, and writing the list of doctors to a file.  
class DoctorManager:
    def __init__(self):
        self.doctors = []
        self.read_doctors_file()

    def format_dr_info(self, obj):
        return f"{obj.doctor_id}_{obj.doctor_name}_{obj.specialization}_{obj.working_time}_{obj.qualification}_{obj.room_number}"

    def enter_dr_info(selfid): #might need to put self in to it
        doctor_id = input("enter the doctor's ID: ")
        doctor_name = input("Enter the doctor's name: ")
        specialization = input("Enter the doctor's specility: ")
        working_time = input("Enter the doctor's timing (e.g., 7am-10pm): ")
        qualification = input("Enter the doctor's qualification: ")
        room_number = input("Enter the doctor's room number: ")
        doctor = Doctor(doctor_id, doctor_name, specialization, working_time, qualification, room_number)
        print(f"\nDoctor whose ID is {doctor_id} has been added.\n")
        return doctor

    def read_doctors_file(self):
        with open('doctors.txt', 'r') as f:
            file_content = f.readlines()
        for line in file_content:
            doctor_data = line.strip('\n').split('_')  #Take a look if i should have \n
            doctor = Doctor(doctor_data[0], doctor_data[1], doctor_data[2], doctor_data[3], doctor_data[4], doctor_data[5])
            self.doctors.append(doctor)

    def search_doctor_by_id(self):
        new_id = input()
        for item in self.doctors:
            if new_id == item.doctor_id:
                return item
        print("Can't find the doctor with the same ID on the system\n")
        return None


    
    def search_doctor_by_name(self):
        found = False
        doctor_name = input("Enter the doctor name: ")
        for doctor in self.doctors:
            if doctor.doctor_name == doctor_name:
                found = True
                print(doctor)
                break
        if not found:
            print("\nCan't find the doctor with the same name on the syestem")

    def display_doctor_info(self):
        print("Enter the doctor Id:")
        obj = self.search_doctor_by_id()
        if obj is not None:
            print(self.doctors[0])
            print(obj)




    def edit_doctor_info(self):
        print("Please enter the id of he doctor that you want to edit their information:")
        obj = self.search_doctor_by_id()
        if obj is not None:
            newdoctorname = input('Enter the new name: ')
            newspecialization = input("Enter the new specialization: ")
            newworking_time = input("Enter the new timing: ")
            newqualification = input("Enter the new qualification: ")
            newroom_number = input("Enter the new room number: ")
            obj.set_doctor_name(newdoctorname)
            obj.set_specialization(newspecialization)
            obj.set_working_time(newworking_time)
            obj.set_qualification(newqualification)
            obj.set_room_number(newroom_number)
            print(f"\nDoctor whose ID is {obj.doctor_id} has been edited.")
            self.write_list_of_doctors_to_file()


    def display_doctors_list(self):
        for item in self.doctors:
            print(item)

    def write_list_of_doctors_to_file(self):
        with open("doctors.txt", "w") as f:
            for item in self.doctors:
                content = self.format_dr_info(item)
                f.write(content)
                f.write("\n")

    def add_dr_to_file(self):
        obj = self.enter_dr_info()
        self.doctors.append(obj)
        self.write_list_of_doctors_to_file()

#This class contains constructor method that initializes the properties of a patient such as their id, name, disease, gender and age.
class Patient:
    def __init__(self,pid=0,name = "",disease = "", gender = "",age = 0 ):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def getPid(self):
        return self.pid

    def getName(self):
        return self.name

    def getDisease(self):
        return self.disease

    def getGender(self):
        return self.gender

    def getAge(self):
        return self.age

    def setPid(self,pid):
        self.pid = pid

    def setName(self,name):
        self.name = name

    def setDisease(self,disease):
        self.disease = disease

    def setGender(self,gender):
        self.gender = gender

    def setAge(self,age):
        self.age = age

    def __str__(self):
        return f"{self.pid}\t{self.name}\t{self.disease}\t{self.gender}\t{self.age}\n"

#This class is another part of a larger system that manages patient's information. It is responsible  for managing a list of patients, adding new patients, Searching for paitneds by Id or name, editing patient information and displaying a list of all patients.
class PatientManager:
    def __init__(self):
        self.patientList = []
        self.read_patients_file()

    def format_patient_Info_for_file(self,obj):
        return f"{obj.pid}_{obj.name}_{obj.disease}_{obj.gender}_{obj.age}"

    def enter_patient_info(selfpid):
        pid = input("Enter Patient id:")
        name = input("Enter Patient name:")
        disease = input("Enter Patient disease:")
        gender = input("Enter Patient gender:")
        age = input("Enter Patient age: ")
        patient = Patient(pid,name,disease,gender,age)
        print(f"\nPatient whose ID is {pid} has been added.\n")
        return patient

    def read_patients_file(self):
        with open("patients.txt", "r") as f:
            file = f.readlines()
        for info in file:
            patientInfo = info.strip('\n').split('_')
            patient = Patient(patientInfo[0], patientInfo[1], patientInfo[2], patientInfo[3], patientInfo[4])
            self.patientList.append(patient)

    def search_patient_by_id(self):
        id = input("Enter the Patient Id: \n")
        for item in self.patientList:
            if id == item.pid:
                return item
        print("Can't find the Patient with the same id on the system\n")
        return None

    def display_patient_info(self):
        obj = self.search_patient_by_id()
        if obj is not None:
            print(self.patientList[0])
            print(obj)

    def edit_patient_info_by_id(self):
        obj = self.search_patient_by_id()
        if obj is not None:
            name = input("Enter new Patient name:")
            disease = input("Enter new Patient disease:")
            gender = input("Enter new Patient gender:")
            age = input("Enter new Patient age: ")
            obj.setName(name)
            obj.setDisease(disease)
            obj.setGender(gender)
            obj.setAge(age)
            print(f"\nPatient whose ID is {obj.pid} has been edited.\n")
            self.write_list_of_patients_to_file()

    def display_patients_list(self):
        for item in self.patientList:
            print(item)

    def write_list_of_patients_to_file(self):

        with open("patients.txt", "w") as f:
            for item in self.patientList:
                content = self.format_patient_Info_for_file(item)
                f.write(content)
                f.write("\n")

    def add_patient_to_file(self):
        obj = self.enter_patient_info()
        self.patientList.append(obj)
        self.write_list_of_patients_to_file()

#this function is responsible for presenting the user with options to select if they want to work on patient or a doctor, and then redirecting the user to the corresponding menu.
def main_menu():
    while True:
        print("Welcome to Alberta Hospital(AH) Managment system")
        print("Select from the following option, or select 3 to stop:")
        print("1-\t Doctors")
        print("2-\t Patients")
        print("3-\t Exit Program")
        choice = input()
        if choice == '1':
            doctors_menu()
        elif choice == '2':
            patients_menu()
        elif choice == '3':
            print("Thanks for using the program,Bye!")
            break
        else:
            print("Invalid choice. Please try again.")

#this function is called when the user selects the opton to work with the doctor whether they want to add new doctor, edit doctor, and  it will call upon a function accordingly
def doctors_menu():
    while True:
        print("Doctors Menu")
        print("1 - Display Doctors List")
        print("2 - Search Doctor by ID")
        print("3 - Search Doctor by name")
        print("4 - Add Doctor")
        print("5 - Edit Doctor Info")
        print("6 - Back to Main Menu")
        choice = input()
        docMenu = DoctorManager()
        if choice == '1':
            docMenu.display_doctors_list()
        elif choice == '2':
            docMenu.display_doctor_info()
        elif choice == '3':
            docMenu.search_doctor_by_name()
        elif choice == '4':
            docMenu.add_dr_to_file()
        elif choice == '5':
            docMenu.edit_doctor_info()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

#This function displays menu for working with patiends, it is called when the user selects the options to access the patients menu. It presents with options to view their age, gender, disease and more which also can be editied.
def patients_menu():
    while True:
        print("Patients Menu")
        print("1 - Display Patients List")
        print("2 - Search Patient by ID")
        print("3 - Add Patient")
        print("4 - Edit Patient Info")
        print("5 - Back to the Main Menu")

        choice = input()
        patMenu = PatientManager()
        if choice == "1":
            patMenu.display_patients_list()
        elif choice == "2":
            patMenu.display_patient_info()
        elif choice == "3":
            patMenu.add_patient_to_file()
        elif choice == "4":
            patMenu.edit_patient_info_by_id()
        elif choice == "5":
            break
        else:
            print("Invalid Choice")

#The initial code starts with this function
main_menu()
