equation = input("Please enter an equation : \n")
left_side_list = equation.split("=")[0]
right_side_list = equation.split("=")[1]

left_side_list = left_side_list + "+"
right_side_list = right_side_list + "+"
left_side_list_x = []
right_side_list_x = []
left_side_list_coe = []
right_side_list_coe = []
for i in range(len(left_side_list)):
    for j in range(len(left_side_list)):
        if j > i:
            if left_side_list[i] == "+":
                if left_side_list[j] == "+" or left_side_list[j] == "-":
                    if left_side_list[j-1] == "x":
                        left_side_list_x.append(left_side_list[i:j-1])
                        break
                    else:
                        left_side_list_coe.append(left_side_list[i:j])
                        break
            elif left_side_list[i] == "-":
                if left_side_list[j] == "-" or left_side_list[j] == "+":
                    if left_side_list[j-1] == "x":
                        left_side_list_x.append(left_side_list[i:j-1])
                        break
                    else:
                        left_side_list_coe.append(left_side_list[i:j])
                        break
for i in range(len(right_side_list)):
    for j in range(len(right_side_list)):
        if j > i:
            if right_side_list[i] == "+":
                if right_side_list[j] == "+" or right_side_list[j] == "-":
                    if right_side_list[j-1] == "x":
                        right_side_list_x.append(right_side_list[i:j-1])
                        break
                    else:
                        right_side_list_coe.append(right_side_list[i:j])
                        break
            elif right_side_list[i] == "-":
                if right_side_list[j] == "-" or right_side_list[j] == "+":
                    if right_side_list[j-1] == "x":
                        right_side_list_x.append(right_side_list[i:j-1])
                        break
                    else:
                        right_side_list_coe.append(right_side_list[i:j])
                        break
left_x = 0
right_coe = 0
for i in left_side_list_x:
    left_x += int(i)

for i in right_side_list_x:
    left_x -= int(i)

for i in right_side_list_coe:
    right_coe += int(i)

for i in left_side_list_coe:
    right_coe -= int(i)
print("The most basic form of your equation is")
print("The most basic form of your equation is "+ str(left_x)+"x="+str(right_coe))
print("So x="+str(right_coe/left_x))






