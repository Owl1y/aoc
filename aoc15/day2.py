
with open("day2.txt", "r") as client_nums:
    lines = client_nums.readlines()
    lines = [line.rstrip() for line in lines]

total_wrap = []

for j in range(len(lines)):
    #res = [i for i in range(len(lines[j])) if lines[i].startswith('x', i)]
    #print(res)
    s = lines[j]
    c = 'x'
    res = [pos for pos, char in enumerate(s) if char == c]
    #print(res)


    lwh = []
    l = int(lines[j][0:res[0]])
    # print(f"length is {l}")
    w = int(lines[j][res[0]+1:res[1]])
    # print(f"width is {w}")
    h = int(lines[j][res[1]+1:])
    # print(f"height is {h}")


    dimension = 2*(l * w) + 2*(w * h) + 2*(h * l)

    lwh = [l,w,h]
    lwh.sort()
    extra_wrap = lwh[0] * lwh[1]
    # print(lwh) 
    total_wrapping = dimension + extra_wrap
    total_wrap.append(total_wrapping)
    # print(sum(total_wrap))


print(sum(total_wrap))
#print(lwh)
#print(dimension)
#print(f"{dimension + extra_wrap}")
#print(total_wrap)
#print(lines[0][0:res[0]-1], lines[0][res[0]:res[1]-1], lines[0][res[1]:])
