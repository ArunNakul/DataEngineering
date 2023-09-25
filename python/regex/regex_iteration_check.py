import re
while True:
    text = input("Input the email id")
    #pattern = input("pattern to be searched")
    #text = " hello Ajay"
    #pattern = r"."
    pattern = r"^(arun)+$"
    match = re.findall(pattern, text)

    print ("match :",match)

    '''
Input the email idarunarunarun
Ans: : ['arun']
Input the email idarunuranraun
Ans:match : []
Input the email id
    '''