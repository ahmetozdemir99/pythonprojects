#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

with open("TaskList.txt") as t:
    task = t.readlines()
    task_list = [] # -->  It's a list that contains the information in "TaskList.txt".
    task_list_remain = []
    for i in task:
        i = i.replace("\n", "")
        i = i.replace(" ", "")
        i = i.split(",")
        task_list.append(i)

#-------- The above codes provided to transfer the data in the task list to the file named task list. --------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    hero_hp = 3000
    pegasus_hp = 550
    walk_speed = 20
    pegasus_speed = 50
    time = 0                # --> Before the program starts, the "time" variable is equal to zero, but as the tasks are done, time will pass and the "time" variable will change accordingly.
    location = ""           # --> The value of this variable will change when hero swaps.
    winner_list = []        # --> This list contains the names of all users who finished this game..
    winner_time_list = []   # --> This list includes the time the game has ended by users who finished the game.
    min_time_list = []      # --> This list contains the names of the 3 fastest players to finish this game.
    min_user_list = []      # --> This list includes the finishing times of the 3 fastest players in this game.
    min_indexes_list = []   # --> This list stores the indexes of the 3 fastest players to finish this game in the winner_list and winner_time_list.

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------ HALL OF FAME LİST --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def hall_of_fame(): # This function first takes the minimum value in the winner_time_list and its index.
                        # Thanks to the index method. It also finds the minimum time person from the winner_list and adds them to the empty lists.
                        # If the number of people who finish the game is equal to 3 or more than 3, it does this 3 times,
                        # If it is less than 3, it does the number of people who finished it, and it prints the names of 3 people with the shortest time.

        print("--------------------------")
        print("| Name    | Finish Time  |")
        print("--------------------------")
        if len(winner_time_list) >= 3:
            for a in range(3):
                minimin = min(winner_time_list) # --> The variable named minimin is the lowest value in the list.
                min_time_list.append(minimin)   # --> This list contains the names of the 3 fastest players to finish this game.
                index = winner_time_list.index(minimin)
                min_user_list.append(winner_list[index])
                winner_list.remove(winner_list[index])
                winner_time_list.remove(minimin)
                print("|", str(min_user_list[a])," "*(6-len(min_user_list[a])),"| ",str(min_time_list[a]),"hour"," "*(5-len(min_time_list[a])),"|")
                print("--------------------------")
        else:
            for i in range(len(winner_time_list)):
                minimin = min(winner_time_list)
                min_time_list.append(minimin)
                index = winner_time_list.index(minimin)
                min_user_list.append(winner_list[index])
                winner_list.remove(winner_list[index])
                winner_time_list.remove(minimin)
                print("|",str(min_user_list[i])," "*(6-len(min_user_list[i])),"| ",str(min_time_list[i]),"hour"," "*(5-len(min_time_list[i])),"|")
                print("--------------------------")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------- RECURSİVE FUNCTİON-1 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                        # I run this function by entering 0 parameters in the mainloop.
                        # Since n equals 0 at the beginning in the function, it prints the first element and recursively increments n by 1.
                        # It continues to do this until n equals the number of items in the task_list.
                        # When n equals the number of items in task_list, the function is terminated.

    def remain_task(n):
        if n == len(task_list):
            pass
        elif n == 0:
            print("Here are the tasks left that hero needs to complete:")
            print("--------------------------------------------------------")
            print("| TaskName | ByFootDistance | ByPegasus | HPNeeded     |")
            print("--------------------------------------------------------")
            print("|", str(task_list[n][0]), "   | ", str(task_list[n][1]), "km",
                  " " * (9 - len(task_list[n][1])), "| ", str(task_list[n][2]),
                  " " * (7 - len(task_list[n][2])), "| ", str(task_list[n][3]),
                  " " * (10 - len(task_list[n][3])), "|")
            print("--------------------------------------------------------")
            return remain_task(n+1)
        else:
            print("|", str(task_list[n][0]), "   | ", str(task_list[n][1]), "km",
                  " " * (9 - len(task_list[n][1])), "| ", str(task_list[n][2]),
                  " " * (7 - len(task_list[n][2])), "| ", str(task_list[n][3]),
                  " " * (10 - len(task_list[n][3])), "|")
            print("--------------------------------------------------------")
            return remain_task(n+1)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------- RECURSİVE FUNCTİON-2 -----------------------------------------------------------------------------------------------------------------------------------------------------------------

                        # I run this function by entering 0 parameters in the mainloop.
                        # When n is not equal to index_task, it recursively calls remove_task by incrementing n by 1 by 1.
                        # When n equals index_task this function removes task_list[index_task] element from task_list.

    def remove_task(n):
        if n == len(task_list):
            pass
        else:
            if n == index_task:
                task_list.remove(task_list[n])
            else:
                remove_task(n+1)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------ FUNCTİONS THAT RETURN INFORMATIONS OUTSİDE OF THE TASKS IN THE "Task.list.txt" FILE. ----------------------------------------------------------------------------------------------

    def distances_pegasus(n):   # -->  This function to know distances by pegasus.
        for i in range(len(task_list)):
            if n == task_list[i][0]:
                return task_list[i][2]


    def distances_walk(m):      # -->  This function to know distances by walk.
        for i in range(len(task_list)):
            if m == task_list[i][0]:
                return task_list[i][1]


    def hp_tokill(m):           # -->  This function is to know HP needed for selected task.
        for i in range(len(task_list)):
            if m == task_list[i][0]:
                return task_list[i][3]

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------- MAİN LOOP --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def mainloop(pegasus_hp,hero_hp):# -->  This function is main function of homework.
        global location
        global time
        global index_task
        print("Welcome to Hero’s 5 Labors!")
        print("Remaining HP for Hero :  ",hero_hp)
        print("Remaining HP for Pegasus:  ",pegasus_hp)
        print("Here are the tasks left that hero needs to complete:")
        print("--------------------------------------------------------")
        print("| TaskName | ByFootDistance | ByPegasus | HPNeeded     |")
        print("--------------------------------------------------------")
        for i in range(len(task_list)):
            print("|",str(task_list[i][0]),"   | ",str(task_list[i][1]),"km"," "*(9-len(task_list[i][1])),"| ",str(task_list[i][2])," "*(7-len(task_list[i][2])),"| ",str(task_list[i][3])," "*(10-len(task_list[i][3])), "|")
        print("--------------------------------------------------------")
        print()
        k = 1
        while k == 1:
            a = input("Where should Hero go next?") # --> a is the task the user wants to select.
            a = a.lower()
            a = a.capitalize()
            hp = hp_tokill(a)        # -->  It is hp needed for selected task.
            index_task = 0           # -->  It is the variable that determines the indexes of the places where the Hero goes.It's new value is always determined in the following loop.
            for i in range(len(task_list)):
                if a == task_list[i][0]:
                    location = a     # --> The value of location changed when hero swaps.
                    k = 2
                    break
                index_task += 1
            else:
                print("Invalid input")
                k = 1
            while k == 2:
                b = input("How do you want to travel?(Foot/Pegasus)") # It is a selection that how user wants to travel.
                b = b.lower()
                distance = distances_walk(location)     #  -->  This variables is the distance that must be walked to accomplish the selected task.
                distance2 = distances_pegasus(location) #  -->  This variable is the distance the pegasus must travel to perform the selected task.
                if hero_hp >= 10*(int(distance) / walk_speed) + int(hp):
                    if b == "foot":
                        if distance == "-1":
                            print("You cannot go there by foot.")
                            k = 2
                        else:
                            print("Hero defeated monster.")
                            hero_hp -= int(hp) + 10*(int(distance) / walk_speed)
                            time += int(distance) / walk_speed  #  -->  Before the program starts, the "time" variable is equal to zero, but as the tasks are done, time will pass and the "time" variable will change accordingly.
                            print("Time passed  :", time, " hour")
                            print()
                            print("Remaining HP for Hero : ",hero_hp)
                            print("Remaining HP for Pegasus:  ",pegasus_hp)
                            print()
                            k = 3
                    elif b == "pegasus":
                        if pegasus_hp >= 15*(int(distance2) / pegasus_speed):
                            hero_hp -= int(hp)                                  # -->  int(hp) is equal to needed hp to kill for selected task.
                            pegasus_hp -= 15*(int(distance2) / pegasus_speed)   # -->  Before the program starts, the health of Pegasus is a constant, but this health is  changing according to the tasks.
                            time += int(distance2) / pegasus_speed              # -->  Before the program starts, the "time" variable is equal to zero, but as the tasks are done, time will pass and the "time" variable will change accordingly.
                            print("Hero defeated monster.")
                            print("Time passed  :", time, " hour")
                            print()
                            print("Remaining HP for Hero : ", hero_hp)
                            print("Remaining HP for Pegasus:  ", pegasus_hp)
                            print()
                            k = 3
                        else:
                            if distance == "-1":
                                print("Game Over")
                                break
                            else:
                                print("Pegasus does not have enough HP.")
                                k = 2
                    else:
                        print("Invalid input")
                        k = 2
                else:
                    print("Game Over")
                    break
                while k == 3:
                    b2 = input("How do you want to go home?(Foot/Pegasus)")     # -->  It is a selection that how user want to go home.
                    b2 = b2.lower() # It's for to be not case-sensitive.
                    distance_ = distances_walk(location)
                    distance2_ = distances_pegasus(location)
                    if b2 == "foot":
                        if hero_hp >= int(hp) + 10*(int(distance_) / walk_speed):
                            if distance_ == "-1":
                                print("You cannot go there by foot.")
                                k = 3
                            else:
                                print("Hero arrived home.")
                                location = "home"   # -->  When hero arrived home I changed location as "home".
                                hero_hp -= 10*(int(distance) / walk_speed)
                                time += int(distance_) / walk_speed
                                print("Time passed  :", time, " hour")
                                print()
                                print()
                                print("Remaining HP for Hero : ", hero_hp)
                                print("Remaining HP for Pegasus:  ", pegasus_hp)
                                print()
                                remove_task(0)
                                remain_task(0)
                                if not task_list: # If there is no member in task_list.
                                    print("Congratulations, you have completed the task.")
                                    name = input("What is your name : ")            # -->  This variable is the name of the person who finished the game.
# -->  The codes from "LİNE-1" to "LİNE-2" transfer the data from the file named Hall_of_fame.txt to empty lists named winner_list and winner_time_list.
# -->  If the file named Hall_of_fame.txt does not exist on the user's computer, it creates a file named Hall_of_fame.txt.
#--------------------------------------- LİNE-1 ------------------------------------------------------------------------
                                    with open("Hall_of_fame.txt", "a") as g:
                                        g.write(name + "," + str(time) + "\n")
                                    with open("Hall_of_fame.txt") as f:
                                        reader = f.readlines()
                                        for i in reader:
                                            i = i.replace("\n", "")
                                            index_comma_l = []
                                            index_comma = 0
                                            for a in i:
                                                if a == ",":
                                                    index_comma_l.append(index_comma)
                                                index_comma += 1
                                            names = i[:index_comma_l[0]]     # -->  Names in "Hall_of_fame.txt".
                                            winner_list.append(names)
                                            times = i[index_comma_l[0] + 1:] # -->  Times in "Hall_of_fame.txt".
                                            winner_time_list.append(times)
#------------------------------------------ LİNE-2 ---------------------------------------------------------------------
                                        hall_of_fame()
                                        break
                                else:
                                    k = 1
                        else:
                            if pegasus_hp >= 15*(int(distance2_) / pegasus_speed):
                                print("You can not go there by walk.")
                                k = 3
                            else:
                                print("Pegasus does not have enogh HP.")
                                print("Game Over")
                                break
                    elif b2 == "pegasus":
                        if pegasus_hp >= 15*(int(distance2_) / pegasus_speed):
                            pegasus_hp -= 15*(int(distance2_) / pegasus_speed)
                            print("Hero arrived home.")
                            location = "home"
                            time += int(distance2_) / pegasus_speed
                            print("Time passed  :  ",time, " hour")
                            print()
                            print("Remaining HP for Hero :  ", hero_hp)
                            print("Remaining HP for Pegasus:  ", pegasus_hp)
                            print()
                            remove_task(0)
                            remain_task(0)
                            if not task_list:
                                print("Congratulations, you have completed the task.")
                                name = input("What is your name : ")
                                with open("Hall_of_fame.txt", "a") as g:
                                    g.write(name + "," + str(time) + "\n")
                                with open("Hall_of_fame.txt") as f:
                                    reader = f.readlines()
                                    for i in reader:
                                        i = i.replace("\n", "")
                                        index_comma_l = []
                                        index_comma = 0
                                        for a in i:
                                            if a == ",":
                                                index_comma_l.append(index_comma)
                                            index_comma += 1
                                        names = i[:index_comma_l[0]]
                                        winner_list.append(names)
                                        times = i[index_comma_l[0] + 1:]
                                        winner_time_list.append(times)
                                    hall_of_fame()
                                    break
                            else: #-->  (If  there is at least 1 member in task_list):
                                k = 1 # --> (Return to the beginning of the loop).
                        else: # -->  (If pegasus HP is not enough to finish to task).
                            if distance_ == "-1" or hero_hp < int(hp) + 10*(int(distance_) / walk_speed):
                                print("Game Over")
                                break
                            else:
                                print("Pegasus does not have enough HP.")
                                k = 3 # -->  It's for select a new departure method from the user.
                    else:
                        print("Invalid input.")
                        k = 3  # -->  It's for select a new departure method from the user.

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
mainloop(pegasus_hp,hero_hp)