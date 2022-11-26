import hashlib

input = "ckczppom"
five0 = "00000"
six0 = "000000"

x = 0
input_num = bytes(input + str(x), 'utf-8')
result = hashlib.md5(input_num)

while str(result.hexdigest())[0:5] != five0:
    x = x + 1
    input_num = bytes(input + str(x), 'utf-8')
    result = hashlib.md5(input_num)
    # print(result.hexdigest())
print(result.hexdigest())
print(x)

# Part 2
while str(result.hexdigest())[0:6] != six0:
    x = x + 1
    input_num = bytes(input + str(x), 'utf-8')
    result = hashlib.md5(input_num)
    # print(result.hexdigest())
print(result.hexdigest())
print(x)


