def getBelts(BeltSec_):
    with open("RecDiameters.txt") as f:
        content = f.readlines()
        l = []
        for i in content:
            d = i.split()
            l.append(d)
        belt_name_list = []
        for i in range(len(l)):
            belt_name_list.append(l[i][0])
    if BeltSec_ in belt_name_list:
        return True


def getMinMax(BeltSec_):
    with open("RecDiameters.txt") as f:
        content = f.readlines()
        l = []
        for i in content:
            d = i.split()
            l.append(d)
    for i in range(len(l)):
        if BeltSec_ == l[i][0]:
            return [l[i][1] ,l[i][2]]

def getDiameters():
    with open("StandardPulleyDiameters.txt") as f:
        content = f.readlines()
        l = []
        for i in content[1:]:
            i = i.replace("\n","")
            l.append(i)
        return l


def calcRatios_Sort(x):
    min = int(getMinMax(x)[0])
    max = int(getMinMax(x)[1])
    avaible_diameters = []
    l = getDiameters()
    ratios = []
    for i in l:
        if int(i) >= min and int(i) <= max:
            avaible_diameters.append(i)
    for i in avaible_diameters:
        for j in l:
            if float(j) / float(i) >= 1:
                ratios.append([float(i), float(j), float(j) / float(i)])
    sorted_ratios = sorted(ratios, key=lambda x: x [2])
    return sorted_ratios

def calcRatios_Unsort(x):
    min = int(getMinMax(x)[0])
    max = int(getMinMax(x)[1])
    avaible_diameters = []
    l = getDiameters()
    ratios = []
    for i in l:
        if int(i) >= min and int(i) <= max:
            avaible_diameters.append(i)
    for i in avaible_diameters:
        for j in l:
            if float(j) / float(i) >= 1:
                ratios.append([float(i), float(j), float(j) / float(i)])
    return ratios

def printSortedRatios(x):
    sorted_ratios = calcRatios_Sort(x)
    with open("Ratios_Sorted.txt","w") as f:
        f.write("Availabe Ratios for Belt Cross-Section\n")
        f.write("D_Small  D_Large   Speed_Ratio\n")
        for i in range(len(sorted_ratios)):
            f.write("%4.f %8.f %14.3f\n" % (sorted_ratios[i][0], sorted_ratios[i][1], sorted_ratios[i][2]))

def printCrossTable(x):
    sorted_ratios = calcRatios_Sort(x)
    unsorted_ratios = calcRatios_Unsort(x)
    rows = []
    column = []
    with open("Cross_Table.txt", "w") as f:
        f.write("Availabe Ratios for Belt Cross-Section\nD_Large")
        for i in range(len(sorted_ratios)):
            rows.append(sorted_ratios[i][1])
            column.append(sorted_ratios[i][0])
        rows = set(rows)
        rows = sorted(rows)
        for i in rows:
            f.write("%8.f" %(i))
        f.write("\nD_small")
        for i in range(len(unsorted_ratios)):
            if unsorted_ratios[i][2] != 1:
                f.write("%8.3f" %unsorted_ratios[i][2])
            else:
                f.write("\n%4.f" %(unsorted_ratios[i][0]) +"        "*i + " %11.3f" %(unsorted_ratios[i][2]))


while True:
    BeltSec = input('Select Belt Section : ')
    if getBelts(BeltSec):
        printSortedRatios(BeltSec)
        printCrossTable(BeltSec)
        break
    else:
        print("Not Valid Belt type!!")