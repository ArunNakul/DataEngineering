import re
while True:
    text = input("Input the email id")
    #pattern = input("pattern to be searched")
    #text = " hello Ajay"
    #pattern = r"."
    pattern = r"^[arun]+$"
    match = re.findall(pattern, text)

    print ("match :",match)

    ''' [] will not check the order or letters in a string
        () will check the order of letters in a string
Input the email idarunarun
match : ['arunarun']
Input the email idarunnruaruarnraun
match : ['arunnruaruarnraun']
Input the email id

    '''