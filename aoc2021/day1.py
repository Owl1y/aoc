M_Increase = 0

with open('day1.txt','r') as f:
    mylist = [int(x) for x in f]

for i, element in enumerate(mylist):
    if i == 0:
        print("first data input lmao")
    elif mylist[i-1] < mylist[i]:
        M_Increase = M_Increase + 1

print(M_Increase)
