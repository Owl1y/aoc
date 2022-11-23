# this only day 3 and bruh how tf do i even start 

with open("day3.txt", "r") as client_nums:
    lines = client_nums.readlines()
    lines = [line.rstrip() for line in lines]

input = lines[0]

coords_of_houses = [[0,0]]
count_x = 0
count_y = 0

for i in input:
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
        
# got info to sort list of list from here https://stackoverflow.com/questions/12198468/how-to-remove-duplicate-lists-in-a-list-of-list
sorted_houses = set(map(tuple,coords_of_houses))
sorted_houses_list = map(list,sorted_houses)

print(len(sorted_houses))

# Part 2

santa_list = []
for n in enumerate(input):
    if n%2 == 0:
        santa_list.append(n)

print(santa_list)


Santa_list = [n for n in range(len(lines[0])) if n%2 == 0]
print(Santa_list)
