#re - > regular expression operation
import re

text = open('Actual_Data.txt')
numlist = []

for line in text:
    # The method rstrip() returns a copy of the string in which
    # all chars have been stripped from the end of the string
    # For example:
    # str = "     this is string example....wow!!!     ";
    # print str.rstrip()
    # str = "88888888this is string example....wow!!!8888888";
    # print str.rstrip('8')(default whitespace characters).
    # Results:
    # this is string example....wow!!!
    # 88888888this is string example....wow!!!
    line = line.rstrip()
    # (	Indicates where string extraction is to start
    # )	Indicates where string extraction is to end
    # +	Repeats a character one or more times
    extract = re.findall('([0-9]+)', line)

    if len(extract) < 1: continue

    for i in range(len(extract)):
        num = float(extract[i])
        numlist.append(num)

print(sum(numlist))
