import re
while True:
    text = input ("Enter the string : ")
    #pattern = r"a{5,10}"  # check 'a' char count is 5,6,7,8,9,10 occuring
    #pattern = r"^a{5,10}$"  # check 'whole' string 'a' char count is 5,6,7,8,9,10 occuring
    pattern = r"^a{5,10}?$"  # check 'whole' string 'a' char count is 5,6,7,8,9 (ignore 10) occuring
    match = re.findall(pattern,text)
    
    print("count : ", len(match))
    print("match : ",match)