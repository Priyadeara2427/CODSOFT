import random
def RandomInt(length, lower, upper):
    pas=""
    for i in range(length):
        s1 = random.randint(lower, upper)
        pas+=chr(s1)
    return pas
def RandomChoice(length, list1):
    pas=""
    for i in range(length):
        s2= random.choice(list1)
        pas+=s2
    return pas
s1 = ["@","!","&","$","%","#","*"]
print(" Password Generator ")
length = int(input("Enter the length of the password: "))
complexity =  input("Enter the complexity of password as simple, moderate or difficult: ")
pas=""
if complexity == "simple":
    ran = RandomInt(length,97,122)
    pas+=ran
elif complexity == "moderate":
    ran = RandomInt(length-3,97,122)
    pas+=ran
    ch = RandomChoice(2, s1)
    pas+=ch
    ran= RandomInt(1,0,9)
    pas+=ran
else:
    v1 = length//2
    v2 = length - v1
    ran = RandomInt(1,65,91)
    pas+=ran
    ran = RandomInt(v1-1,97,122)
    pas+=ran  
    ch = RandomChoice(1,s1)
    pas+=ch
    v2-=1
    ran = RandomInt(v2//2,0,9)
    pas+=ran 
    ch = RandomChoice(1,s1)
    pas+=ch
    fi_len = length - len(pas)
    ran = RandomInt(fi_len,97,122)
    pas+=ran 
print("The password generated is:\n",pas)
    