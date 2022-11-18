with open("day2.txt", "r") as client_nums:
    lines = client_nums.readlines()
    lines = [line.rstrip() for line in lines]

total_wrap = []
ribben_wrap = []
for j in range(len(lines)):
    
    #found at https://dev.to/jules_lewis/advent-of-code-2015-day-2-ek4
    l, w, h = map(int, lines[j].split('x'))
    
    lwh = []
    dimension = 2*(l * w) + 2*(w * h) + 2*(h * l)
    
    #sorting the length width and height to multiply by the smallest two values 
    lwh = [l,w,h]
    lwh.sort()
    # adding the whole value 
    extra_wrap = lwh[0] * lwh[1]
    total_wrapping = dimension + extra_wrap
    total_wrap.append(total_wrapping)
    
    # for ribben part 2
    ribben_bow = l * w * h
    ribben = lwh[0] + lwh[0] + lwh[1] + lwh[1]
    ribben_total = ribben_bow + ribben
    ribben_wrap.append(ribben_total)


print(sum(total_wrap))
print(sum(ribben_wrap))
