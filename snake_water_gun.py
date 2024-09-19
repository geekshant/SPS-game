import random
computer = random.randint(-1,1)

you = input("enter your choice: ")
youdict = {"s":1, "w":-1, "g":0}
reversedict = {1 :"s", 0 : "g", -1 : "w"}
younum = youdict[you]

if(computer == -1 and younum == 1):
    print(F"computer choice: {reversedict[computer]} younumr choice : {reversedict[younum]}, you won")
elif(computer == -1 and younum == -1):
    print(F"computer choice: {reversedict[computer]} your choice : {reversedict[younum]}, draw")
elif(computer == -1 and younum == 0):
    print(F"computer choice: {reversedict[computer]} your choice : {reversedict[younum]}, computer won")
elif(computer == 0 and younum == 0):
    print(F"computer choice: {reversedict[computer]} your choice : {reversedict[younum]}, draw")
elif(computer == 0 and younum == 1):
    print(F"computer choice: {reversedict[computer]} your choice : {reversedict[younum]}, computer won")
elif(computer == 0 and younum == -1):
    print(F"computer choice: {reversedict[computer]} your choice : {reversedict[younum]}, you won")
elif(computer == 1 and younum == 1):
    print(F"computer choice: {reversedict[computer]} your choice : {reversedict[younum]}, draw")
elif(computer == 1 and younum == 0):
    print(F"computer choice: {reversedict[computer]} your choice : {reversedict[younum]}, you won")
elif(computer == 1 and younum == -1):
    print(F"computer choice: {reversedict[computer]} your choice : {reversedict[younum]}, computer won")
elif(computer == you):
    print("it's a draw")
else:
    print("something went wrong")
print() 