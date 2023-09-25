import re
while True:
    text = input("Enter the string : ")
 
    #pattern = r"^(arun){3}$"   => arun in 3 times
    #pattern = r"^(arun|ajay){2,2}$"  => arun or ajay in 2 times
    pattern = r"^[a-z0-9]\.{2,5}$"  #first character either a to z or 0 to 9 with . and . can be 2 times or 5 times
    #pattern = r"^arun[.]$"

    match = re.findall(pattern, text)

    print ("match :",match)