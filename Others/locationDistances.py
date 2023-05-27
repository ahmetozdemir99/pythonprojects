travel_types =["CAR","MOTORCYCLE","BICYCLE"]
cities_l = []
province_x_l = []
province_y_l = []
distances_l = []
distances_l_2 = []
english_words = ["Q","W","X"]
min_dist_list =[]
min_city_list =[]
indexes_list = []
with open("provinces.txt") as p:
    city_provinces = p.readlines()
    for i in city_provinces:
        i = i.replace("\n"," ")
        index_comma_l =[]
        index_comma = 0
        counter = 0
        for a in i:
            if a == ",":
                index_comma += 1
                index_comma_l.append(counter)
            counter += 1
        cities = i[:index_comma_l[0]]
        cities_l.append(cities)
        provinces = i[index_comma_l[0] + 1 :]
        province_x = provinces.split(",")[0]
        province_x_l.append((province_x))
        province_y = provinces.split(",")[1]
        province_y_l.append(province_y)
    q = 1
    while q == 1:
        departure_province = input("Departure province:\n")
        departure_province = departure_province.upper()
        if departure_province not in cities_l:
            q = 1
            print("Province not found!")
            c = ""
            m = len(departure_province)
            controller_1 = 0
            if departure_province in english_words:
                q = 1
            else:
                for i in sorted(cities_l):
                    if i[:m] == departure_province:
                        c += i + ","
                        c += ""
                        t = "Possible province:{}" .format(c)
                        t_2 = "Possible provinces:{}" .format(c)
                        t = t[:len(t) - 1]
                        t_2 = t_2[:len(t_2) -1]
                        controller_1 += 1
                if controller_1 != 0:
                    if ","in t:
                        print(t_2)
                    else:
                        print(t)
                    controller_1 = 0
        else:
            q = 2
        while q == 2:
            arrival_province = input("Arrival province:\n")
            arrival_province = arrival_province.upper()
            if arrival_province not in cities_l:
                q = 2
                print("Province not found!")
                w = ""
                u = len(arrival_province)
                controller_2 = 0
                for i in sorted(cities_l):
                    if i[:u] == arrival_province:
                        w += i + ","
                        w += ""
                        r = "Possible province:{}" .format(w)
                        r_2 = "Possible provinces:{}" .format(w)
                        r = r[:len(r) -1]
                        r_2 = r_2[:len(r_2) - 1]
                        controller_2 += 1
                if controller_2 != 0:
                    if "," in r:
                       print(r_2)
                    else:
                        print(r)
                    controller_2 = 0
            elif arrival_province == departure_province:
                q = 2
                print("Enter a different province!")
            else:
                q = 3
            while q == 3 :
                travel_type = input("Enter travel type:\n")
                travel_type = travel_type.upper()
                if travel_type in travel_types:
                    q = 4
    count_1 = 0
    for city in cities_l:
        if city != departure_province:
            count_1 += 1
        elif city == departure_province:
            x_province_departure = float(province_x_l[count_1])
            y_province_departure = float(province_y_l[count_1])
            count_2 = 0
    for cityy in cities_l:
        if cityy != arrival_province:
            count_2 += 1
        elif cityy == arrival_province:
            x_province_arrival = float(province_x_l[count_2])
            y_province_arrival = float(province_y_l[count_2])
    n = 0
    for i in range (81):
        if cities_l[n] == departure_province:
            break
        n += 1
    for i in range (81):
        distances = (((float(province_x_l[n]) - float(province_x_l[i]))**2 + (float(province_y_l[n]) - float(province_y_l[i]))**2)** 0.5) * 100
        distances_l.append(float(distances))
        distances_l_2.append(float(distances))
    for i in range(4):
        minimin = min(distances_l)
        min_dist_list.append(minimin)
        indexes = distances_l_2.index(minimin)
        indexes_list.append(indexes)
        distances_l.remove(minimin)
    for i in indexes_list[1:]:
        min_city_list.append(cities_l[i])
    min_city_list.sort()
    distance = (((x_province_arrival - x_province_departure)**2 + (y_province_arrival - y_province_departure) **2) **0.5) * 100
    time_car = distance / 90
    hour_car = int(time_car)
    min_car = int((time_car - hour_car) * 60)
    time_motorcylce = distance / 80
    hour_motorcycle = int(time_motorcylce)
    min_motorcycle = int((time_motorcylce - hour_motorcycle) * 60)
    time_bicycle = distance / 25
    hour_bicycle = int(time_bicycle)
    min_bicycle = int((time_bicycle - hour_bicycle) * 60)
    travel_hour = 0
    travel_min = 0
    if travel_type == "CAR":
        travel_hour += hour_car
        travel_min += min_car
    elif travel_type == "MOTORCYCLE":
        travel_hour += hour_motorcycle
        travel_min += min_motorcycle
    elif travel_type == "BICYCLE":
        travel_hour += hour_bicycle
        travel_min += min_bicycle
    print()
    print("I am calculating the distance between" ,departure_province,"and" ,arrival_province,"...")
    print()
    print("Distance:" ,round(distance ,2) ,"km")
    print("Approximate travel time with",travel_type+":",travel_hour,"hours",travel_min,"minutes")
    print("Recommended places close to " + departure_province + ":" + min_city_list[0] + "," + min_city_list[1]+ "," + min_city_list[2])