# Patient Database in nested list
patient = [
    [7001,'SABRINA GORDON', 'FEMALE',44, 'INSURANCE', 'COLLIN HEYE', 17, 'NORMAL', 'DIABET'],
    [7002,'MIA THERMOPOLIS', 'FEMALE', 56, 'PRIVATE', 'SHIRLEY HANKIN', 26, 'HYPERTENSION', 'DIABET'],
    [7003,'ZAYN WILLEND', 'MALE', 47, 'BPJS', 'KELLY SWANSEN', 20, 'HYPOTENSION', 'DIABET'],
    [7004,'EMA WINSTON', 'FEMALE',40, 'BPJS', 'COLLIN HEYE', 19, 'NORMAL', 'NO DIABET'],
    [7005,'JEREMY BARNARD', 'MALE',38, 'PRIVATE', 'SHIRLEY HANKIN', 28, 'NORMAL', 'DIABET'],
    [7006,'MERLE GLOVER', 'MALE',36, 'INSURANCE', 'KELLY SWANSEN', 19, 'HYPERTENSION', 'NO DIABET'],
]

patientColumn = ['ID', 'Name', 'Gender', 'Age','Payment', 'Doctor', 'BMI', 'Blood Pressure', 'Diabetic Conditions']

# Patient database access is limited, must input access password
def accessPassword() :
    welcome = 'Welcome to Mentari Hospital, Please Input Database Access Password'
    print(welcome.upper())
    while True :
        numAccess = input('Please input access password : ')
        if numAccess == '1379luck':
            print('Hello, Welcome to Patient Database')
            break
        else :
            print('Please input the right access Password.')
accessPassword()

# show all databases
def showAllDatabases():

    # Block code to create column of table containing title of column patient database
    # icon | and - as table line
    print(110 *'-')
    print('|',patientColumn[0],'','|', patientColumn[1], 7*' ','|', patientColumn[2],'|', patientColumn[3],'|', patientColumn[4],' ','|',patientColumn[5],4*' ','|', patientColumn[6],'|', patientColumn[7],'|', patientColumn[8],'|')
    print(110 *'-')

    # using 'for loop' to show all database in range of patient list
    for i in patient:
        column1 = i[0]
        column2 = i[1] 
        column3 = i[2]
        column4 = i[3]
        column5 = i[4]
        column6 = i[5]
        column7 = i[6]
        column8 = i[7]
        column9 = i[8]

        # Block code to create table
        # | as line + column index + (the length of the column with the longest data value - len of column --> will be different for each row)

        print('| '+ str(column1) + (4-len(str(column1)))*" "
            +'| ' + column2 + (15-len(column2))*" "
            +'| ' + column3 + (6-len(column3))*" "
            +'| ' + str(column4) + (3- len(str(column4)))*" "
            +'| ' + column5 + (9- len(column5))*" "
            +'| ' + column6 + (14 - len(column6))*" "
            +'| ' + str(column7) + (4 - len(str(column7)))*" "
            +'| ' + column8 + (14 - len(column8))*" "
            +'| ' + column9 + (19 - len(column9))*" "
            +'  |')
    # Block code to create line of the table    
    print(110*"-")
    # recall read function
    readPatientData()

# read based on patient ID (primary column)
def showBasedID() :
    inputID = int(input('Please enter patient ID number : '))

    # initial index is 0
    patientIndex = 0
    totalIndex = len(patient) - 1
    
    # using for loop to do iteration read all patient on condition was given
    for index in patient :
        trueID = index[0] # ID in index[0] in each list
        if inputID == trueID :
            print(f'{patientColumn[0]} = {trueID}')
            print(f'{patientColumn[1]} = {index[1]}')
            print(f'{patientColumn[2]} = {index[2]}')
            print(f'{patientColumn[3]} = {index[3]}')
            print(f'{patientColumn[4]} = {index[4]}')
            print(f'{patientColumn[5]} = {index[5]}')
            print(f'{patientColumn[6]} = {index[6]}')
            print(f'{patientColumn[7]} = {index[7]}')
            print(f'{patientColumn[8]} = {index[8]}')
            break # to stop looping because the data has been found

        elif inputID != trueID and totalIndex == patientIndex : # if list of ID did not found in all index of patient nested list
            print('Please enter the right patient ID')
            showBasedID() # recall show based ID function
        patientIndex += 1 # to read patient data from first to last
    readPatientData() # recall read function

# read based on Doctor
def showBasedDoctor() :
    inputDoctor = input('Please enter Doctor Name : ')

    # initial index is 0
    patientIndex = 0
    totalIndex = len(patient) - 1

    # using for loop to do iteration read all patient on condition was given
    for index in patient :
        trueDoctor = index[5] # doctor in index[5] in each list
        if inputDoctor.upper() == trueDoctor : # using upper() in case input of user is in lowercase
            print(f'{patientColumn[0]} = {index[0]}')
            print(f'{patientColumn[1]} = {index[1]}')
            print(f'{patientColumn[2]} = {index[2]}')
            print(f'{patientColumn[3]} = {index[3]}')
            print(f'{patientColumn[4]} = {index[4]}')
            print(f'{patientColumn[5]} = {trueDoctor}')
            print(f'{patientColumn[6]} = {index[6]}')
            print(f'{patientColumn[7]} = {index[7]}')
            print(f'{patientColumn[8]} = {index[8]}')
            print('-'*50)
            continue # for skip next block code (if doctor name input wrong)
        patientIndex += 1 # to show all patients with the same doctor's name, not stopping at the earliest patient

        if inputDoctor.upper() != trueDoctor and totalIndex == patientIndex : # if list of doctor did not found in all index of patient nested list
            print('Please enter the right Doctor name')
            showBasedDoctor() # recall show based doctor function
    readPatientData() # recall read function

# read based on payment
def showBasedPayment() :
    inputPayment = input('Please enter Payment Method : ')
    
    # initial index is 0
    patientIndex = 0
    totalIndex = len(patient) - 1

    # using for loop to do iteration read all patient on condition was given
    for index in patient :
        truePayment = index[4] # doctor in index[4] in each list
        if inputPayment.upper() == truePayment : # using upper() in case input of user is in lowercase
            print(f'{patientColumn[0]} = {index[0]}')
            print(f'{patientColumn[1]} = {index[1]}')
            print(f'{patientColumn[2]} = {index[2]}')
            print(f'{patientColumn[3]} = {index[3]}')
            print(f'{patientColumn[4]} = {truePayment}')
            print(f'{patientColumn[5]} = {index[5]}')
            print(f'{patientColumn[6]} = {index[6]}')
            print(f'{patientColumn[7]} = {index[7]}')
            print(f'{patientColumn[8]} = {index[8]}')
            print('-'*50)
            continue # for skip next block code (if payment method input wrong)
        patientIndex += 1 # to show all patients with the same payment method, not stopping at the earliest patient
        if inputPayment.upper() != truePayment and totalIndex == patientIndex : # if list of payment did not found in all index of patient nested list
            print('Please enter the right payment method')
            showBasedPayment()
    readPatientData()

# read patient data
def readPatientData() :
    while True :
        print('''Choose option for show patient database
              1. Show all databases
              2. Show based on patient ID
              3. Show based on doctor
              4. Show based on payment
              5. Back to main menu''')
        numberMenu = int(input('Choose your options = '))
        if numberMenu == 1 :
            showAllDatabases()
            break
        elif numberMenu == 2 :
            showBasedID()
            break
        elif numberMenu == 3 :
            showBasedDoctor()
            break
        elif numberMenu == 4 :
            showBasedPayment()
            break
        elif numberMenu == 5 :
            mainMenu()
            break
        else :
            print('The option you entered is not valid, please input only the numbers are provided in the following options')

# Create Patient Data
def addNewPatient():
    while True :
        print('''Please choose option =
              1. Add new patient
              2. Back to main menu''')
        numberMenu = int(input('Choose your options = '))
        if numberMenu == 1 :
            ID = int(input('Enter new patient ID number : '))
            while True :
                # cehck if ID is in list of patient
                if ID == patient[0][0] or ID == patient[1][0] or ID == patient[2][0] or ID == patient[3][0] or ID == patient[4][0] or ID == patient[5][0]:
                    print('Data already exists')
                    addNewPatient()
                    break
                else :
                    Name = input('Enter patient name : ').upper() # using lower() (following writing model in database) in case input of user is not in uppercase 
                    Gender = input ('Enter patient gender : ').upper()
                    Age = int(input ('Enter patient age, just number (ex: 30, 42): '))
                    Payment = input ('Enter payment method: ').upper()
                    Doctor = input('Enter doctor name : ').upper()
                    BMI = int(float(input('Enter Patient BMI (ex : 18) : ')))
                    BloodPressure = input('Enter patient blood pressure condition : ').upper()
                    DiabetCon = input('Enter diabetic condition patient : ').upper()
                    save = input('Are you sure want to save data? (yes/no)')

                    addPatient = [ID, Name, Gender, Age, Payment, Doctor, BMI, BloodPressure, DiabetCon]
                        
                    if save.lower() == 'no' : # using lower() in case input of user is not in lowercase
                        mainMenu()
                        break
                    elif save.lower() == 'yes': # using lower() in case input of user is not in lowercase
                        patient.append(addPatient)
                        print('Data has been added, please check on patient database')
                        readPatientData()
                        break
        elif numberMenu == 2 :
            mainMenu()
            break
        else :
            print('The option you entered is not valid, please input only the number provided in the following options')

#Update Patient Data
def UpdatePatientData() :
    while True :
        print('''Please choose option =
              1. Update/Edit patient data
              2. Back to main menu''')
        numberMenu = int(input('Choose your options = '))
        if numberMenu == 1 :
            # show database based on ID
            patientIndex = 0
            totalIndex = len(patient) - 1
            inputID = int(input('Please enter Patient ID : '))
            for index in patient :
                trueID = index[0] # ID always in index[0] in each list
                patientIndex += 1 # to read patient data from first to last in nested list
                if inputID != trueID and totalIndex == patientIndex :
                    print('Please enter the right patient ID')
                    UpdatePatientData()
                elif inputID == trueID :
                    print(f'{patientColumn[0]} = {trueID}')
                    print(f'{patientColumn[1]} = {index[1]}')
                    print(f'{patientColumn[2]} = {index[2]}')
                    print(f'{patientColumn[3]} = {index[3]}')
                    print(f'{patientColumn[4]} = {index[4]}')
                    print(f'{patientColumn[5]} = {index[5]}')
                    print(f'{patientColumn[6]} = {index[6]}')
                    print(f'{patientColumn[7]} = {index[7]}')
                    print(f'{patientColumn[8]} = {index[8]}')
                    
                    while True :
                        inputUpdate = input('Continue update data? (yes/no) ')
                        if inputUpdate == 'no' :
                            mainMenu()
                            break
                        elif inputUpdate == 'yes' :
                            #ask what column that want to update
                            columnInput = int(input(' 1. Name \n 2. Gender \n 3. Age \n 4. Payment \n 5. Doctor \n 6. BMI \n 7. Blood Pressure \n 8. Diabetic Conditions \n Enter the number of column (just number): '))
                            #ask for the new value
                            valueInput = input('Input new value information : ').upper()
                            if inputID != trueID and totalIndex == patientIndex :
                                print('The data you are looking for does not exists, please enter the right patient ID')
                                UpdatePatientData()
                            elif inputID == trueID :
                                while True :
                                    save = input('Are you sure want to update data? (yes/no)')
                                    if save == 'no' :
                                        mainMenu()
                                        break
                                    elif save == 'yes' :
                                        # block code for find exact index of patient ID in each list
                                        def patientIndex(patient, updateID):
                                            for index, patient in enumerate(patient):
                                                if patient[0] == updateID:
                                                    return index
                                                
                                        updateID = inputID
                                        index = patientIndex(patient, updateID)
                                        patient[index][columnInput] = valueInput

                                        updateMore = input('Do you also want to update other data? (yes/no) : ')
                                        if updateMore.lower() == 'yes' :
                                            UpdatePatientData()
                                        elif updateMore.lower() == 'no' :
                                            readPatientData()
                                        break
        elif numberMenu == 2 :
            mainMenu()
            break
        else :
            print('The option you entered is not valid, please input only the number provided in the following options')

# Delete Patient Data
def deletePatientData() :
    while True :
        print('''Please choose option =
              1. Delete patient data
              2. Back to main menu''')
        numberMenu = int(input('Choose your options = '))
        if numberMenu == 1 :
            inputID = int(input('Please enter Patient ID : '))

            #initial index is 0
            patientIndex = 0
            totalIndex = len(patient) - 1
            
            # using for loop to do iteration read patient on condition was given
            for index in patient :
                trueID = index[0] # ID always in index[0] in each list
                patientIndex += 1 # to read patient data from first to last in nested list
                if inputID != trueID and totalIndex == patientIndex :
                    print('The data you are looking for does not exists, please enter the right patient ID')
                    deletePatientData()
                elif inputID == trueID :
                    # block code for find exact index of patient ID in each list
                    def patientIndex(patient, deleteID):
                        for index, patient in enumerate(patient):
                            if patient[0] == deleteID:
                                return index
                        
                    deleteID = inputID
                    index = patientIndex(patient, deleteID)

                    confirm = input('Are you sure want to delete data? (yes/no) : ').lower()
                    if confirm == 'no' :
                        mainmenu()
                    elif confirm == 'yes':
                        patient.pop(index) # removes the patient data at the specified index
                        print('Data successfully deleted, please check on patient database')
                        readPatientData()
        elif numberMenu == 2 :
            mainMenu()
            break
        else :
            print('The option you entered is not valid, please input only the number provided in the following options')
# main menu CRUD
def mainMenu() :
    while True :
        numberMenu = 'Patient Database Menu \n 1. Create or Add New Patient Data \n 2. Read Patient Data \n 3. Update or Edit Patient Data \n 4. Delete Patient Data \n 5. Exit'
        print(numberMenu)
        choose = int(input('Please Input The Number Menu : '))
        if choose == 1 :
            addNewPatient()
            break
        elif choose == 2 :
            readPatientData()
        elif choose == 3 :
            UpdatePatientData()
            break
        elif choose == 4 :
            deletePatientData()
            break
        elif choose == 5 :
            print('Thank you, have a great day!')
            break
        else :
            print('The option you entered is not valid, please input only the number provided in the main menu')
mainMenu()

