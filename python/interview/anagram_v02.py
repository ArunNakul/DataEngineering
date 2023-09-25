#inp1 = 'listen'
#inp2 = 'silent'

inp1 = input("Enter the first string")
print (inp1)

inp2 = input("Enter the first string")
print (inp2)


x = [inp1[i] for i in range(0,len(inp1))]
x.sort()

y = [inp2[i] for i in range(0,len(inp2))]
y.sort()



print ("x :",x)
print ("y : ", y)

if (x == y):
    print("This is Anagram")
else:
    print("This is not Anagram")