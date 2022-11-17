
with open("day2input.txt", "r") as client_nums:
    lines = client_nums.readlines()
    lines = [line.rstrip() for line in lines]

total_wrap = 0

for j in range(len(lines)):
    res = [i for i in range(len(lines[j])) if lines[j].startswith('x', i)]

    lwh = []
    l = int(lines[0][0:res[0]-1])
    w = int(lines[0][res[0]:res[1]-1])
    h = int(lines[0][res[1]:])

    dimension = 2*(l * w) + 2*(w * h) + 2*(h * l)

    lwh = [l,w,h]
    lwh.sort()
    extra_wrap = lwh[0] * lwh[1]
    print(lwh) 
    total_wrap = dimension + extra_wrap


#print(lwh)
#print(dimension)
print(f"{dimension + extra_wrap}")
print(total_wrap)
#print(lines[0][0:res[0]-1], lines[0][res[0]:res[1]-1], lines[0][res[1]:])
