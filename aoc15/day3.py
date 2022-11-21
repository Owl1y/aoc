# this only day 3 and bruh how tf do i even start 

with open("day3.txt", "r") as client_nums:
    lines = client_nums.readlines()
    lines = [line.rstrip() for line in lines]


coords_of_houses = []
# x_axis = 0
# y_axis = 0
count_x = 0
count_y = 0

for i in lines[0]:
    if i == '>':
        count_x = count_x + 1
    if i == '<':
        count_x = count_x - 1
    if i == '^':
        count_y = count_y + 1
    if i == 'v':
        count_y = count_y - 1
        


sum_east = lines[0].count('>')
sum_west = lines[0].count('<')
sum_north = lines[0].count('^')
sum_south = lines[0].count('v')

# print(f"North is {sum_north}\nEast is {sum_east}\nSouth is {sum_south}\nWest is {sum_west}")

print((sum_north * sum_east) - (sum_south * sum_west))
print( count_y, count_x)





