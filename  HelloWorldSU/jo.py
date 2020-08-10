# Inputlar al
course = input("Please enter filename for the courses list: ")
final = input("Please enter filename for the finals list: ")


#1. Dictionary oluştur
kurslar=open(course, "r")
kurslarL=kurslar.readlines()
dict1 = {}
for element in kurslarL:
    kursLine=element.splitlines()[0].split(" ")
    k = kursLine[0]
    kursLine.remove(kursLine[0])
    if k not in dict1:
        dict1[k] = kursLine
    else:
        dict1[k] += kursLine
kurslar.close()


#2. Dictionary oluştur
finaller=open(final, "r")
finallerL=finaller.readlines()
dict2=dict()
for element in finallerL:
    finalLine = element.splitlines()[0].split("\t")
    k = finalLine[0]
    finalLine.remove(finalLine[0])
    if k not in dict2:
        dict2[k] = finalLine
    else:
        dict2[k] += finalLine

finaller.close()


#Kimlik doğru mu kontrol et
def inputCheck(x,y):
    if x in y:
        a = True
    else:
        a = False
    return a

#kimlik kontrol gbt
kimlik = input("Please enter a student ID: ")

while inputCheck(kimlik, dict1) == False:


    print("There is no student with ID " + kimlik)

    kimlik = input("Please enter a student ID: ")

print("Final exam schedule of student with ID ", kimlik, ":", sep="")


#Kursları var mı yok mu diye ayırma işlemi yapan fonksiyon

def findCourses(list, dict, a, b):
    for element in list:
        if element in dict:
            var.append(element)
        else:
            yok.append(element)

var = []
yok = []
kursListe = dict1[kimlik]
findCourses(kursListe, dict2, var, yok)

tarih = []
zaman = []

#Tarih ve zaman listeleri oluştur
for z in var:
    tarih.append(dict2[z][1])
    zaman.append(dict2[z][2])

xtarih = []
xzaman = []

#Dictionary de ikisini birleştir
for dict1 in tarih:
    xtarih.append(dict1.replace(".", ""))
for q in zaman:
    xzaman.append(q.replace(":", ""))
for w in xzaman:
    xzaman[xzaman.index(w)] = w.replace("-", "")
combined = [p + q for p, q in zip(xtarih, xzaman)]

#key value oluştur
yeniDict = {}
for k in combined:
    for x in var:
        yeniDict[k] = x
        var.remove(x)
        break

combined.sort()


#olan kursları yaz
for element in combined:
    print("\t".join(dict2[yeniDict[element]]))

#olmayan kursları yaz

if yok!=[]:
    print("Courses without a final exam:", ", ".join(yok))
