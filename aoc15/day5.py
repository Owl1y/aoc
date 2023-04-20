import re

with open("day5.txt", "r") as client_nums:
    lines = client_nums.readlines()
    lines = [line.rstrip() for line in lines]

nice_words = 0
for i in range(len(lines)):
    # these two used for regex extraction 
    # https://www.tutorialspoint.com/extract-only-characters-from-given-string-in-python
    # https://stackoverflow.com/questions/41562828/find-vowels-using-regex#41562945
    cut_v = "".join(re.findall("[aAeEiIoOuU]+", lines[i]))
    # for double letters, https://stackoverflow.com/questions/1023902/it-is-possible-to-match-a-character-repetition-with-regex-how 
    double_let = "".join(re.findall(r"(.)\1+", lines[i]))
    
    forb_ab = lines[i].find("ab")
    forb_cd = lines[i].find("cd")
    forb_pq = lines[i].find("pq")
    forb_xy = lines[i].find("xy")
    forb_let = [forb_ab, forb_cd, forb_pq, forb_xy] 
    forb_let_cut = [*set(forb_let)] 

    if (len(cut_v) >= 3) and (len(double_let) >= 1) and (len(forb_let_cut) == 1):
        #print(f"{lines[i]}   {cut_v}    {double_let}   {len(double_let)}    {forb_let_cut}    {len(forb_let_cut)}")
        nice_words = nice_words + 1 

print(nice_words)

# Part 2
# I spent hours and hours on part two and gave in and went to the reddit to find the answer
# using this post https://old.reddit.com/r/adventofcode/comments/3viazx/day_5_solutions/cxnt6bp/

count = sum(
      1 for s in lines
      if len(re.findall(r"([a-z]{2}).*\1", s))
      and re.findall(r"([a-z]).\1", s)
 )
print(count)
