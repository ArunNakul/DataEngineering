import re
while True:
    text = input("Enter the string : ")
 
    #pattern = r"^(arun){3}$"
    #pattern = r"^(arun|ajay){2,2}$"
    pattern = r"^arun\.$"
    #pattern = r"^arun[.]$"

    match = re.findall(pattern, text)

    print ("match :",match)