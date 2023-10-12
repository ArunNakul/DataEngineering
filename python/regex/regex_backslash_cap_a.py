import re

while True:
    text = input("Enter the String :")

    pattern = r"\Z" # doubt
    pattern = r"\AA[\w\s]*n\Z" # Good One -> it checks the multiple line strings , for example #Ajay Check the first 'A' character and
                                                                                               #Arun     and end character 'n'
                                                                                               # check absolute start and absolure end


    file1 =open("myfileA.txt","r+")


    text1 = file1.read()

    match = re.findall(pattern,text1)

    print("match : ",match)