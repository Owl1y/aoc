import re

with open("day5.txt", "r") as client_nums:
    lines = client_nums.readlines()
    lines = [line.rstrip() for line in lines]

# vowl = ['a', 'e', 'i', 'o', 'u']
nice_words = 0

for i in range(len(lines)):
    # these two used for regex extraction 
    # https://www.tutorialspoint.com/extract-only-characters-from-given-string-in-python
    # https://stackoverflow.com/questions/41562828/find-vowels-using-regex#41562945
    cut_v = "".join(re.findall("[aAeEiIoOuU]+", lines[i]))
    # for double letters, https://stackoverflow.com/questions/1023902/it-is-possible-to-match-a-character-repetition-with-regex-how 
    double_let = "".join(re.findall(r"(.)\1+", lines[i]))
    
    # forbidden_let = "".join(re.findall(r"\b(?:ab|cd|pq|xy)\b", lines[i]))
    # forb_let = lines[i].find()
    if ("ab" or "cd" or "pq" or "xy") not in lines[i] and len(cut_v) >= 3 and len(double_let) == 1:
        nice_words = nice_words + 1

# print(cut_v, double_let, lines[i], forbidden_let)
print(nice_words)
