M_Increase = 0

with open('day1.txt','r') as f:
    mylist = [int(x) for x in f]

for i, element in enumerate(mylist):
    if i == 0:
        print("first data input lmao")
    elif mylist[i-1] < mylist[i]:
        M_Increase = M_Increase + 1

print(M_Increase)

sumlist = []
testlist = [199, 200, 208, 210, 200, 207, 240, 269, 260,263]


for j, element in enumerate(mylist):
    if j == 0:
        print("nope")
    else:
        sumlist.append(sum(mylist[j-1:j+2:1]))
print(sumlist)

sum_increase = 0

for k, element in enumerate(sumlist):
    if k == 0:
        print("first data input lmao")
    elif sumlist[k-1] < sumlist[k]:
        sum_increase = sum_increase + 1

print(sum_increase)
