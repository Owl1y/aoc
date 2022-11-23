with open("day3.txt", "r") as client_nums:
    lines = client_nums.readlines()
    lines = [line.rstrip() for line in lines]

def cords_fun(directions):
    count_x = 0
    count_y = 0
    coords_of_houses = [[0,0]]
    for i in directions:
        if i == '>':
            count_x = count_x + 1
            coords_of_houses.append([count_x, count_y])
        if i == '<':
            count_x = count_x - 1
            coords_of_houses.append([count_x, count_y])
        if i == '^':
            count_y = count_y + 1
            coords_of_houses.append([count_x, count_y])
        if i == 'v':
            count_y = count_y - 1
            coords_of_houses.append([count_x, count_y])

    return coords_of_houses

def listToString(the_list):
    str1 = ""
    return (str1.join(the_list))

# Part 1
input = lines[0]
part1 = cords_fun(input)
       
# got info to sort list of list from here https://stackoverflow.com/questions/12198468/how-to-remove-duplicate-lists-in-a-list-of-list
sorted_houses = set(map(tuple,part1))
sorted_houses_list = map(list,sorted_houses)
print(f"the houses santa goes to is {len(sorted_houses)}")

# Part 2
santa_list = []
robo_list = []
for n in range(len(input)):
    if n%2 == 0:
        santa_list.append(input[n])
    else:
        robo_list.append(input[n])

santas_houses = cords_fun(listToString(santa_list))
robo_houses = cords_fun(listToString(robo_list))

combined = santas_houses + robo_houses
combined_cut = set(map(tuple, combined))

print(f"houses from robot and santa is {len(combined_cut)}")
