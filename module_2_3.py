my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
positiv_my_list =[]
for list in my_list:
    if list > 0:
        positiv_my_list.append(list)
    else:
        if list == 0:
            continue

        break

print(positiv_my_list)



























#print("Число положительное: ")
#if my_list[0 : -1] > 0:
