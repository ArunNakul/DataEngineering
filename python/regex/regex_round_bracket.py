import re

while True:

    text = input ("Enter the String : ")

    pattern = r"(dsf)" # only check the pattern 'dsf' together is available or not

    match = re.findall(pattern,text)

    print("match : ",match)