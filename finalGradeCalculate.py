print("Welcome to program calculating your final grade must be taken to pass the lesson")
visaPercent = int(input("Grade effect of visa in percent: "))
visaGrade =int(input("Enter your visa grade: "))
visaGrade = int((visaGrade*visaPercent)/10)
finalGrade = 10

for finalGrade in range(1001):

    passingGrade = int(((finalGrade*(100-visaPercent))/100)+visaGrade)

    if (passingGrade==600):
     finalGrade = finalGrade/10
     finalGrade = round(finalGrade, 0)
     finalGrade = finalGrade+1
     print("Final grade you must take to pass: "+str(finalGrade))
     break

