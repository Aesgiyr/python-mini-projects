print("Welcome to university grade calculator")

while True:
    visaPercent = int(input("Grade effect of visa in percent: "))
    visaGrade=int(input("Enter your visa grade: "))
    finalGrade=int(input("Enter your final grade: "))
    mainGrade=(((visaGrade*visaPercent)/100)+((finalGrade*(100-visaPercent))/100))
    mainGrade = round(mainGrade,0)

    if (visaGrade>100 or visaGrade<0 or finalGrade<0 or finalGrade>100):
        print("Please enter valid note")
        continue
    elif (mainGrade>90):
        print("Your grade: "+ str(mainGrade))
        print("Congrats, you take AA")
    elif (mainGrade>80):
        print("Your grade: " + str(mainGrade))
        print("Congrats, you take BA")
    elif (mainGrade>70):
        print("Your grade: "+ str(mainGrade))
        print("Congrats, you take BB")
    elif (mainGrade>60):
        print("Your grade: "+ str(mainGrade))
        print("Congrats, you take CB")
    elif (mainGrade>50):
        print("Your grade: " + str(mainGrade))
        print("Congrats, you take CC")
    elif (mainGrade>40):
        print("Your grade: "+ str(mainGrade))
        print("The note you took CD\n You have a conditional right to pass ")
    elif (mainGrade>35):
        print("Your grade: "+ str(mainGrade))
        print("You stayed. Your grade DD")
    elif (mainGrade> 30):
        print("Your grade: "+ str(mainGrade))
        print("You stayed. Your grade DF")
    elif (mainGrade<31):
        print("Your grade: "+ str(mainGrade))
        print("You stayed. Your grade FF")
    islem=int(input("Enter 1 to calculate again\nfor exit enter another key: "))
    if (islem==1):
        continue
    else:
        print("Logging out...")
        break

