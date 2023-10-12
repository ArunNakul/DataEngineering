import re
while True:
    text = input("Enter the string : ")
 
    #pattern = r"^(arun){3}$"   # satisfy the condition when the string contains 'arunarunarun' (3 times)
    #pattern = r"^(arun|ajay){2,2}$"
    #pattern = r"^arun\.$"   # satisfy the condition when the string is starts with 'arun.'  
    pattern = r"^arun[.]$"

    match = re.findall(pattern, text)

    print ("match :",match)