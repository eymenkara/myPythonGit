def makeDict(list, split):
    d = {}
    for i in list:
        line = i.splitlines()[0].split(split)
        key = line[0]
        line.remove(line[0])
        if key not in d:
            d[key] = line
        else:
            d[key] += line
    return d


input1 = input("Please enter filename for the courses list: ")
input2 = input("Please enter filename for the finals list: ")

courses = open(input1, "r")
courseList = courses.readlines()
courseDict = makeDict(courseList, " ")
courses.close()

finals = open(input2, "r")
fL = finals.readlines()
finalsDict = makeDict(fL, "\t")
finals.close()


studentID = input("Please enter a student ID: ")
while studentID not in courseDict:
    print("There is no student with ID " + studentID)
    studentID = input("Please enter a student ID: ")

print("Final exam schedule of student with ID " + studentID + ":")


#Seperate courses with no finals
coursesList = courseDict[studentID]
yes = []
no = []
for i in coursesList:
    if i in finalsDict:
        yes.append(i)
    else:
        no.append(i)

dates = []
times = []
dates1 = []
times1 = []

#Seperate date and time
for z in yes:
    dates.append(finalsDict[z][1])
    times.append(finalsDict[z][2])
for d in dates:
    dates1.append(d.replace(".", ""))
for t in times:
    times1.append(t.replace(":", ""))
for t in times1:
    times1[times1.index(t)] = t.replace("-", "")
res = [i + j for i, j in zip(dates1, times1)]


xdict = dict(zip(res, yes))

res.sort()

for i in res:
    print("\t".join(finalsDict[xdict[i]]))

if not no == []:
    print("Courses without a final exam: " + ", ".join(no))
