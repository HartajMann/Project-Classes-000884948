class Doctor:

    def readDoctorsFile(self, filename="doctors.txt"):
        doctorList = []
        with open(filename, 'r') as file:
            for lines in file:
                lines = lines.rstrip('\n')
                lines = lines.split('_')
                doctorList.append(lines)
        return doctorList

    def displayDoctorsList(self, doctorList):
        x = ' '
        for lines in doctorList:
            print(lines[0] + 15 * x + lines[1] + 15 * x + lines[2] + 15 * x + lines[3] + 15 * x + lines[4] + 15 * x +
                  lines[5])

    def searchDoctorById(self, doctorList):
        x = ' '
        id = input("Enter the doctor Id:\n")
        for lines in doctorList:
            if id == lines[0]:
                print("Id" + x * 10, "Name" + x * 10, "Speciality" + x * 10, "timing" + x * 10,
                      "Qualification" + x * 10, "Room Number")
                print(lines[0] + x * 10, lines[1] + x * 10, lines[2] + x * 10, lines[3] + x * 10, lines[4] + x * 10,
                      lines[5])
        if id != lines[0]:
            print("Wrong id entered")

    def searchDoctorByName(self, doctorList):
        x = ' '
        name = input("Enter doctor name:\n")
        for lines in doctorList:
            if name == lines[1]:
                print("Id" + x * 10, "Name" + x * 10, "Speciality" + x * 10, "timing" + x * 10,
                      "Qualification" + x * 10, "Room Number")
                print(lines[0] + x * 10, lines[1] + x * 10, lines[2] + x * 10, lines[3] + x * 10, lines[4] + x * 10,
                      lines[5])
        if name != lines[1]:
            print("Wrong name entered")

    def editDoctorInfo(self, doctorList):
        id = input("Please enter the id of the doctor that you want to edit their information:")
        for lines in doctorList:
            if id == lines[0]:
                lines[1] = input("Enter new Name:")
                lines[2] = input("Enter new Specilist in:")
                lines[3] = input("Enter new Timing:")
                lines[4] = input("Enter new Qualification:")
                lines[5] = input("Enter new Room number:")
                index = doctorList.index(lines)
                doctorList[index] = lines
                return doctorList

    def addDrToFile(self, doctorList):
        self.id = input("Enter the doctor’s ID:")
        self.name = input("Enter the doctor’s name:")
        self.speciality = input("Enter the doctor’s specility:")
        self.timing = input("Enter the doctor’s timing (e.g., 7am-10pm):")
        self.qualification = input("Enter the doctor’s qualification:")
        self.roomNumber = input("Enter the doctor’s room number:")
        newInfo = [self.id, self.name, self.speciality, self.timing, self.qualification, self.roomNumber]
        doctorList.append(newInfo)
        return doctorList

    def formatDrInfo(self, doctorList):
        x = ''
        for lines in doctorList:
            line = lines[0] + '_' + lines[1] + '_' + lines[2] + '_' + lines[3] + '_' + lines[4] + '_' + lines[
                5] + '\n'
            x = x + line
        return x

    def writeListOfDoctorsToFile(self, x):
        filename = 'doctors.txt'
        with open(filename, 'w') as file:
            file.write(x)
