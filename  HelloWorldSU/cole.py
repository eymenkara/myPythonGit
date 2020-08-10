
#get course text
courseInput = input("Please enter filename for the courses list: ")
#get finals text
finalInput = input("Please enter filename for the finals list: ")

#Turn text into dictionary

def properize(givenList, x):
    dictionary = dict()

    for index in givenList:
        l = index.splitlines()[0]
        nile = l.split(x)

        keyOfDict = nile[0]
        nile.remove(nile[0])

        if keyOfDict in dictionary:
            dictionary[keyOfDict] += nile
        else:
            dictionary[keyOfDict] = nile

    return dictionary


#Read and modify courses text

coursesText = open(courseInput, "r")

listOfCourses = coursesText.readlines()

#Turn courses text into dictionary
dCourse = properize(listOfCourses, " ")

coursesText.close()

#Read and modify finals text

finalsText = open(finalInput, "r")

listOfFinals = finalsText.readlines()

#Turn finals text into dictionary
dFinals = properize(listOfFinals, "\t")

finalsText.close()


def checkValidity(id):
    if id not in dCourse:
        return False
    else:
        return True

#Get ID
iD = input("Please enter a student ID: ")

#Check ID
while not checkValidity(iD):
    print("There is no student with ID " + iD)
    iD = input("Please enter a student ID: ")

print("Final exam schedule of student with ID ", iD , ":", sep="")

listC = dCourse[iD]
coursesWithFinal = list()
coursesWithoutFinal = list()

for i in listC:

    if i in dFinals:
        coursesWithFinal.append(i)

    else:
        coursesWithoutFinal.append(i)

#Initial Lists
finalDate = list()
finalTime = list()

#Modified Lists
newDate = list()
newTime = list()

#Get useful data from the dictionary
for element in coursesWithFinal:
    finalDate.append(dFinals[element][1])
    finalTime.append(dFinals[element][2])

for f in finalDate:
    newDate.append(f.replace(".", ""))

for index in finalTime:
    newTime.append(index.replace(":", ""))

for index in newTime:
    newTime[newTime.index(index)] = index.replace("-", "")

mix = [first + second for first, second in zip(newDate, newTime)]

tag = {a: b for a, b in zip(mix, coursesWithFinal)}

#Sort courses according to date and time

mix.sort()

#Course Schedule

for i in mix:
    print("\t".join(dFinals[tag[i]]))

#Courses with no finals
def isEmpty(list):
    if list == []:
        return False
    else:
        return True

if isEmpty(coursesWithoutFinal):
    print("Courses without a final exam: " + ", ".join(coursesWithoutFinal))
