userlist = []
passwordlist = []
friendlist = []
numbers = "0123456789"
letters = "qwertyuıopasdfghjklzxcvbnm"


def reader_login():
    with open("users.txt") as f:
        usernames = f.readlines()
        for i in usernames:
            i = i.replace("\n", "")
            index_semicolon_l = []
            index_semicolon = 0
            counter = 0
            for a in i:
                if a == ";":
                    index_semicolon += 1
                    index_semicolon_l.append(counter)
                counter += 1
            if index_semicolon != 0:
                users = i[:index_semicolon_l[0]]
                if users not in userlist:
                    userlist.append(users)
                    passwords = i[index_semicolon_l[0] + 1: index_semicolon_l[1]]
                    passwordlist.append(passwords)
                    friends = i[index_semicolon_l[1] + 1:]
                    friendlist.append(friends)
        f.close()


def displaymenu():
    print("1. Log in / change user")
    print("2. Create new user")
    print("3. Add friend")
    print("4. Show my friends")
    print("5. Exit")


def menuloop():
    while True:
        my_list = ["1","2","3","4","5"]
        displaymenu()
        options = input()
        if options in my_list:
            break
        else:
            print("Invalid option\n")
            break
    return options


def login():
    name_wanted = input("Please enter username:\n")
    password_wanted = input("Please enter password:\n")
    reader_login()
    for i in range(len(userlist)):
        if name_wanted in userlist:
            if name_wanted == userlist[i]:
                if password_wanted == passwordlist[i]:
                    print("Logged in\n")
                    user_controll = name_wanted
                    return user_controll
                else:
                    print("Wrong password or username\n")
                    user_controll = ""
                    return user_controll
        else:
            print("Wrong password or username\n")
            user_controll = ""
            return user_controll


def showfriends(user_controll):
    reader_login()
    for i in range(len(userlist)):
        if userlist[i] == user_controll:
            print(friendlist[i])
            break


def mainloop():
    user_controll = ""
    while True:
        option = menuloop()
        if option == "1":
            user_controll = login()
        elif option == "2":
            createuser()
        elif option == "3":
            if user_controll == "":
                print("You need to log in first\n")
            else:
                addfriend(user_controll)
        elif option == "4":
            if user_controll == "":
                print("You need to log in first\n")
            else:
                showfriends(user_controll)
        elif option == "5":
            reader_login()
            with open("users.txt","w") as g:
                for i in range(len(userlist)):
                    g.write(userlist[i] + ";" + passwordlist[i] + ";" + friendlist[i] + "\n")
            break


def validatepassword(password_creater):
    if (len(password_creater) <= 8) and (len(password_creater) >= 4):
        for i in password_creater:
            for j in letters:
                if i == j:
                    for x in password_creater:
                        for y in numbers:
                            if x == y:
                                return True
    else:
        return False


def validateusername(name_creater):
    if name_creater not in userlist:
        if name_creater == name_creater.lower():
            for i in name_creater:
                for j in letters:
                    if i == j:
                        return True
            for x in name_creater:
                for y in numbers:
                    if x == y:
                        return True
    else:
        return False


def createuser():
    reader_login()
    name_creater = input("Please enter username:\n")
    if validateusername(name_creater):
        password_creater = input("Please enter password:\n")
        if validatepassword(password_creater):
            counter = 0
            for i in userlist:
                if i == name_creater:
                    if password_creater not in passwordlist[counter]:
                        print("Username not valid\n")
                        break
                else:
                    userlist.append(name_creater)
                    passwordlist.append(password_creater)
                    friendlist.append("")
                counter += 1
                break
        else:
            print("Password not valid\n")
            return name_creater, password_creater
    else:
        print("Username not valid\n")
        return name_creater


def addfriend(user_controll):
    if user_controll in userlist:
        for i in range(len(userlist)):
            if userlist[i] == user_controll:
                addedfriend = input("Please enter the name of your new friend:\n")
                if addedfriend in userlist:
                    if friendlist[i] == "":
                        friendlist[i] += addedfriend
                        break
                    else:
                        friendlist[i] += "," + addedfriend
                        break
                else:
                    print("Friend not found\n")
                    break


mainloop()