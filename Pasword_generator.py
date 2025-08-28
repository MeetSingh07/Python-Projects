# Random Password Generator

import random

password_lst=[]

uppercase_alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_alphabets="abcdefghijklmnopqrstuvwxyz"

numbers="0123456789"

special_characters="@#$&*_"

to_fill_characters="0123456789@#$&*_"

loop="running"

purpose=input("For which app or service you are generating a password ? : ")

while loop=="running":
    try:
        n=int(input("How many characters long you want to generate a password? : "))
        if n<=3:
            print("Please Choose atleast 4 characters.")
        else:
            loop="stop"
    except ValueError:
        print("Please enter an integer value")

for i in range(1,int((30/100)*n)+1):
    password_lst.append(random.choice(uppercase_alphabets))

for i in range(1,int((20/100)*n)+1):
    password_lst.append(random.choice(numbers))

for i in range(1,int((30/100)*n)+1):
    password_lst.append(random.choice(lowercase_alphabets))

for i in range(1,int((20/100)*n)+1):
    password_lst.append(random.choice(special_characters))

if len(password_lst)!=n:
    for i in range(1,n-len(password_lst)+1):
        password_lst.append(random.choice(to_fill_characters))

random.shuffle(password_lst)

password_str=''.join(password_lst)

print(password_str)

f=open("passwords.txt","a")
f.write(f"Purpose -> {purpose} , Password -> {password_str}\n")
f.close()