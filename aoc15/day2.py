
with open("day2.txt", "r") as client_nums:
    lines = client_nums.readlines()
    lines = [line.rstrip() for line in lines]

total_wrap = []
ribben_wrap = []
for j in range(len(lines)):
    s = lines[j]
    c = 'x'
    res = [pos for pos, char in enumerate(s) if char == c]

    lwh = []
    l = int(lines[j][0:res[0]])
    w = int(lines[j][res[0]+1:res[1]])
    h = int(lines[j][res[1]+1:])

    dimension = 2*(l * w) + 2*(w * h) + 2*(h * l)
    
    

    lwh = [l,w,h]
    lwh.sort()

    # for ribben part 2
    ribben_bow = l * w * h
    ribben = lwh[0] + lwh[0] + lwh[1] + lwh[1]
    ribben_total = ribben_bow + ribben
    ribben_wrap.append(ribben_total)

    extra_wrap = lwh[0] * lwh[1]
    total_wrapping = dimension + extra_wrap
    total_wrap.append(total_wrapping)


print(sum(total_wrap))
print(sum(ribben_wrap))
#print(lwh)
#print(dimension)
#print(f"{dimension + extra_wrap}")
#print(total_wrap)
#print(lines[0][0:res[0]-1], lines[0][res[0]:res[1]-1], lines[0][res[1]:])
