import random
print(" Password Generator ")
length = int(input("Enter the length of the password: "))
complexity =  input("Enter the complexity of password as simple, moderate or difficult: ")
pas=""
if complexity == "simple":
    for i in range(length):
        s1 = random.randint(97,122)
        pas+=chr(s1)
elif complexity == "moderate":
    for i in range(length-3):
        s1= random.randint(97,122)
        pas+=chr(s1)
    for i in range(2):
        s1 = ["@","!","&","$","%","#","*"]
        s2= random.choice(s1)
        pas+=s2
    s1= random.randint(0,9)
    pas+=str(s1)
else:
    v1 = length//2
    v2 = length - v1
    for i in range(1):
        s1= random.randint(65,91)
        pas+=chr(s1)
    for i in range(v1-1):
        s1= random.randint(97,122)
        pas+=chr(s1)
    s1 = ["@","!","&","$","%","#","*"]
    s2= random.choice(s1)
    pas+=s2
    v2-=1
    for i in range(v2//2):
        s1= random.randint(0,9)
        pas+=str(s1)
    s1 = ["@","!","&","$","%","#","*"]
    s2= random.choice(s1)
    pas+=s2
    fi_len = length - len(pas)
    for i in range(fi_len):
        s1= random.randint(97,122)
        pas+=chr(s1)
print("The password generated is:\n",pas)
    




    
    



