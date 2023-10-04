import re

while True:

    text = input("Enter the string : ")

    #pattern = r"^\w+$"
    #pattern = r"\w+"
    #pattern = r"^[a-zA-Z0-9\_]$"
    #pattern = r"[a-zA-Z0-9\_]"   # \w is same as [a-zA-Z0-9\_]
 # split the email id into 2 parts, before @ and after @
    #pattern = r"\w+"
    pattern = r"[a-zA-Z0-9\_\.]+"
    #pattern = r"(\w+[\.]{1}\w+)+"
    #pattern = r"(\w+[\.]*)+"

    match = re.findall(pattern,text)

    print("match : ",match)

    print("count : " ,len(match))
