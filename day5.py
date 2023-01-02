
print("hello {}, your balance is {}.".format("ADAM", 230))
print("hello {name}, your balance is {blc}.".format(name="ADAM", blc=230))
print("hello {0}, your balance is {1}.".format("ADAM", 230))
print("hello {1}, your balance is {0}.".format("ADAM", 230))

a= 12
b= 13
c= 18
print(f"this is me {a} from {b} i am {c} years old")

print(f"{0:.60f}")
print(f"{0.6+0.2:.60f}")
print(f"{0.3:.60f}")


a=123
b=complex(a)
print(b)

import pdb
bike1 = "yamaha"
bike1_price = 25000

bike2 = "honda"
bike2_price = 50000

pdb.set_trace()
name = input("enter your name: ")
choose = int(input("press 1 for yamaha and 2 for honda:"))
print(f"hello{name}")

if choose==1:
    print(f"{bike1} will cost you {bike1_price}")
elif choose==2:
    print(f"{bike2} will cost you {bike2_price+2000}")
else:
    print("press only 1 or 2")






