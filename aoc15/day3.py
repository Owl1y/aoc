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


input = lines[0]
part1 = cords_fun(input)
       
# got info to sort list of list from here https://stackoverflow.com/questions/12198468/how-to-remove-duplicate-lists-in-a-list-of-list
sorted_houses = set(map(tuple,part1))
sorted_houses_list = map(list,sorted_houses)
print(f"the houses santa goes to is {len(sorted_houses)}")

# Part 2

# input =  "^v"         # -> 3
input =  "^>v<"       # -> 3
# input =  "^v^v^v^v^v" # -> 11

santa_list = []
robo_list = []
for n in range(len(input)):
    if n%2 == 0:
        santa_list.append(input[n])
    else:
        robo_list.append(input[n])

# print(f"entire input lenght {len(input)} \nsantas list {len(listToString(santa_list))} \nrobo list {len(listToString(robo_list))}")

santas_houses = cords_fun(listToString(santa_list))
robo_houses = cords_fun(listToString(robo_list))
print(santa_list, robo_list)

combined = santas_houses + robo_houses

for swag in range(len(santas_houses)):
    print(santas_houses[swag], robo_houses[swag] )

santas_houses_cut = set(map(tuple,santas_houses))
robo_houses_cut = set(map(tuple, robo_houses))
combined_cut = set(map(tuple, combined))


print(f"houses from robot and santa is {(len(santas_houses_cut) + len(robo_houses_cut)) - 1}")
# its not 2498, 2499, 8193



