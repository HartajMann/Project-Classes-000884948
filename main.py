from classes import Doctor
print("Welcome to Alberta Hospital (AH) Managment system")
no = input(
    "Select from the following options, or select 0 to stop:\n1-Doctors\n2-Facilities\n3-Laboratories\n4-Patients\n")
if no == "1":
    i = 0
    a = Doctor()
    while i != 6:
        doctorList = a.readDoctorsFile()
        no2 = input("Doctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by "
                   "name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n")
        if no2 == '1':
            a.displayDoctorsList(doctorList)
            print("Back to the prevoius Menu")
        elif no2 == '2':
            a.searchDoctorById(doctorList)
            print("Back to the prevoius Menu")
        elif no2 == '3':
            a.searchDoctorByName(doctorList)
            print("Back to the prevoius Menu")
        elif no2 == '4':
            newInfo = a.addDrToFile(doctorList)
            x = a.formatDrInfo(newInfo)
            a.writeListOfDoctorsToFile(x)
            print("Back to the prevoius Menu")
        elif no2 == '5':
            newInfo = a.editDoctorInfo(doctorList)
            x = a.formatDrInfo(newInfo)
            a.writeListOfDoctorsToFile(x)
            print("Back to the prevoius Menu")
        elif no2 == '6':
            quit()
        else:
            print("Wrong no enterd try again.")
            print("Back to the prevoius Menu")
else:
    print("Wrong Entry Try Again.")
    quit()
