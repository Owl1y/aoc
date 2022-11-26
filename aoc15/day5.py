with open("day5.txt", "r") as client_nums:
    lines = client_nums.readlines()
    lines = [line.rstrip() for line in lines]

nice_words = 0
for i in range(len(lines)):
    print(sorted(lines[i]))

