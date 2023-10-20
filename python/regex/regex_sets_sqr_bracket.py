import re

while True:

    text = input("Enter the string : ")

    pattern = r"[\w]"
    pattern = r"^[amk]$"  # either one of the character (a,m,k) is available then it will match
    pattern = r"^[amk]{3}$" # combination of a,m,k should match, for example aaa,amk,kkk

    match = re.findall(pattern,text)

    print("match : ",match)

    print("count : ",len(match))