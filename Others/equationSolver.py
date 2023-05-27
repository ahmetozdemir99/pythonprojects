    eq1 = input("Enter the first equation:\n")
eq2 = input("Enter the second equation:\n")
lseq1 = eq1.split("=")[0]
rseq1 = eq1.split("=")[1]
lseq2 = eq2.split("=")[0]
rseq2 = eq2.split("=")[1]
x_coefficient_list_1 = []
y_coefficient_list_1 = []
coefficient_list_1 = []
x_coefficient_list_2 = []
y_coefficient_list_2 = []
coefficient_list_2= []
x_coefficient_1 = 0
y_coefficient_1 = 0
coefficient_1 = 0
x_coefficient_2 = 0
y_coefficient_2 = 0
coefficient_2 = 0
lseq1 = lseq1 + "%"
rseq1 = rseq1 + "%"
lseq2 = lseq2 +"%"
rseq2 = rseq2 + "%"
for i in range(len(lseq1)):
    if(lseq1[i] == 'x'):
        k = i-1
        while(k>=0):
            if(lseq1[k] == '+' or lseq1[k]== '-' or k == 0):
                x_coefficient_1 = x_coefficient_1 + int(lseq1[k:i])
                break
            k = k - 1
    elif(lseq1[i] == 'y'):
        k = i-1
        while(k>=0):
            if(lseq1[k] == '+' or lseq1[k]== '-' or k == 0):
                y_coefficient_1 = y_coefficient_1 + int(lseq1[k:i])
                break
            k = k - 1
    elif(lseq1[i] == '+' or lseq1[i] == '-'):
        k = i + 1
        while(lseq1[k] != 'x' and lseq1[k] != 'y'):
            if(lseq1[k] == '+' or lseq1[k] == '-'):
                coefficient_1 = coefficient_1 + int(lseq1[i:k])
                break
            elif(lseq1[k] == "%"):
                coefficient_1 = coefficient_1 + int(lseq1[i:k])
                break
            k = k + 1
for i in range(len(rseq1)):
    if(rseq1[i] == 'x'):
        k = i-1
        while(k>=0):
            if(rseq1[k] == '+' or rseq1[k]== '-' or k == 0):
                x_coefficient_1 = x_coefficient_1 - int(rseq1[k:i])
                break
            k = k - 1
    elif(rseq1[i] == 'y'):
        k = i-1
        while(k>=0):
            if(rseq1[k] == '+' or rseq1[k]== '-' or k == 0):
                y_coefficient_1 = y_coefficient_1 - int(rseq1[k:i])
                break
            k = k - 1
    elif(rseq1[i] == '+' or rseq1[i] == '-'):
        k = i + 1
        while(rseq1[k] != 'x' and rseq1[k] != 'y'):
            if(rseq1[k] == '+' or rseq1[k] == '-'):
                coefficient_1 = coefficient_1 - int(rseq1[i:k])
                break
            elif(rseq1[k] == "%"):
                coefficient_1 = coefficient_1 - int(rseq1[i:k])
                break
            k = k + 1
for i in range(len(lseq2)):
    if(lseq2[i] == 'x'):
        k = i-1
        while(k>=0):
            if(lseq2[k] =='+' or lseq1[k]== '-' or k == 0):
                x_coefficient_2 = x_coefficient_2 + int(lseq2[k:i])
                break
            k = k - 1
    elif(lseq2[i] == 'y'):
        k = i-1
        while(k>=0):
            if(lseq2[k] == '+' or lseq2[k]== '-' or k == 0):
                y_coefficient_2 = y_coefficient_2 + int(lseq2[k:i])
                break
            k = k - 1
    elif(lseq2[i] == '+' or lseq2[i] == '-'):
        k = i + 1
        while(lseq2[k] !='x' and lseq2[k] != 'y'):
            if(lseq2[k] == '+' or lseq2[k] == '-'):
                coefficient_2 = coefficient_2 + int(lseq2[i:k])
                break
            elif(lseq2[k] == "%"):
                coefficient_2 = coefficient_2 + int(lseq2[i:k])
                break
            k = k + 1
for i in range(len(rseq2)):
    if(rseq2[i] == 'x'):
        k = i-1
        while(k>=0):
            if(rseq2[k] =='+' or rseq2[k]=='-' or k == 0):
                x_coefficient_2 = x_coefficient_2 - int(rseq2[k:i])
                break
            k = k - 1
    elif(rseq2[i] == 'y'):
        k = i-1
        while(k>=0):
            if(rseq2[k] == '+' or rseq2[k]== '-' or k == 0):
                y_coefficient_2 = y_coefficient_2 - int(rseq2[k:i])
                break
            k = k - 1
    elif(rseq2[i] == '+' or rseq2[i] == '-'):
        k = i + 1
        while(rseq2[k] !='x' and rseq2[k] != 'y'):
            if(rseq2[k] == '+' or rseq2[k] == '-'):
                coefficient_2 = coefficient_2 - int(rseq2[i:k])
                break
            elif(rseq2[k] == "%"):
                coefficient_2 = coefficient_2 - int(rseq2[i:k])
                break
            k = k + 1
x_coefficient_list_1.append(x_coefficient_1)
y_coefficient_list_1.append(y_coefficient_1)
coefficient_list_1.append(-coefficient_1)
x_coefficient_list_2.append(x_coefficient_2)
y_coefficient_list_2.append(y_coefficient_2)
coefficient_list_2.append(-coefficient_2)
if y_coefficient_list_1[0] >= 0:
    y_coefficient_list_1[0] = str(y_coefficient_list_1[0])
    y_coefficient_list_1[0] = "+" + y_coefficient_list_1[0]
if y_coefficient_list_2[0] >= 0:
    y_coefficient_list_2[0] = str(y_coefficient_list_2[0])
    y_coefficient_list_2[0] = "+" + y_coefficient_list_2[0]
print("Equations in the simplified form:")
equ_1 = "{0}x{1}y={2}"
equ_2 = "{0}x{1}y={2}"
print(equ_1.format(x_coefficient_list_1[0], y_coefficient_list_1[0], coefficient_list_1[0]))
print(equ_2.format(x_coefficient_list_2[0], y_coefficient_list_2[0], coefficient_list_2[0]))
x_coefficient_list_1[0] = int(x_coefficient_list_1[0])
x_coefficient_list_2[0] = int(x_coefficient_list_2[0])
y_coefficient_list_1[0] = int(y_coefficient_list_1[0])
y_coefficient_list_2[0] = int(y_coefficient_list_2[0])
coefficient_list_1[0] = int(coefficient_list_1[0])
coefficient_list_2[0] = int(coefficient_list_2[0])
y_solut = int(((x_coefficient_list_1[0] * coefficient_list_2[0]) - (coefficient_list_1[0] * x_coefficient_list_2[0])) / ((x_coefficient_list_1[0] * y_coefficient_list_2[0]) - (y_coefficient_list_1[0] * x_coefficient_list_2[0])))
x_solut = int(((coefficient_list_2[0] * y_coefficient_list_1[0]) - (y_coefficient_list_2[0] * coefficient_list_1[0])) / ((y_coefficient_list_1[0] * x_coefficient_list_2[0]) - (y_coefficient_list_2[0] * x_coefficient_list_1[0])))
solutt = "Solution:\nx={0}\ny={1}"
print(solutt.format(x_solut, y_solut))